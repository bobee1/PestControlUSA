// Cloudflare Pages Function: POST /api/lead
// Sends contact-form leads by email through Resend.
// Required environment variables (Cloudflare Pages > Settings > Variables):
//   RESEND_API_KEY   - Resend API key
//   LEAD_TO_EMAIL    - inbox that receives leads
//   LEAD_FROM_EMAIL  - verified sender, e.g. "PestHalt Leads <leads@pesthalt.us>"

const json = (obj, status = 200) =>
  new Response(JSON.stringify(obj), { status, headers: { "Content-Type": "application/json" } });

const clean = (v, max = 500) => String(v || "").replace(/[<>]/g, "").trim().slice(0, max);

export async function onRequestPost({ request, env }) {
  let data;
  try {
    data = await request.json();
  } catch {
    return json({ ok: false, error: "Invalid request." }, 400);
  }
  if (data.website) return json({ ok: true }); // honeypot: silently accept bots

  const lead = {
    name: clean(data.name, 120),
    phone: clean(data.phone, 40),
    zip: clean(data.zip, 10),
    state: clean(data.state, 40),
    service: clean(data.service, 80),
    message: clean(data.message, 2000),
  };
  if (!lead.name || !/\d{7,}/.test(lead.phone.replace(/\D/g, "")) || !/^\d{5}/.test(lead.zip)) {
    return json({ ok: false, error: "Please enter your name, a valid phone number and ZIP code." }, 400);
  }
  if (!env.RESEND_API_KEY || !env.LEAD_TO_EMAIL || !env.LEAD_FROM_EMAIL) {
    return json({ ok: false, error: "The form is not available right now. Please call instead." }, 503);
  }

  const text = Object.entries(lead).map(([k, v]) => `${k}: ${v}`).join("\n") +
    `\nsubmitted: ${new Date().toISOString()}\nip-country: ${request.headers.get("cf-ipcountry") || ""}`;

  const res = await fetch("https://api.resend.com/emails", {
    method: "POST",
    headers: { Authorization: `Bearer ${env.RESEND_API_KEY}`, "Content-Type": "application/json" },
    body: JSON.stringify({
      from: env.LEAD_FROM_EMAIL,
      to: env.LEAD_TO_EMAIL.split(",").map((s) => s.trim()),
      subject: `PestHalt lead: ${lead.service} - ${lead.zip} ${lead.state}`,
      text,
    }),
  });
  if (!res.ok) return json({ ok: false, error: "Could not send right now. Please call instead." }, 502);
  return json({ ok: true });
}

export const onRequestGet = () => json({ ok: false, error: "Method not allowed." }, 405);
