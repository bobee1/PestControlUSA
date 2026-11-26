"""Trust and legal pages: disclaimer, editorial policy, privacy, terms, accessibility."""
import core as S


def _legal(url, h1, title, meta, doc_line, sections):
    crumbs = [("Home", "/"), (h1, url)]
    hero = (f'<section class="hero page-hero"><div class="wrap">{S.crumbs_html(crumbs)}<h1>{h1}</h1>'
            f'<p class="lead">Last updated {S.TODAY_LONG}</p></div></section>')
    body = f'<div class="wrap"><div class="content legal" style="max-width:900px"><p class="doc">{doc_line}</p>{sections}</div></div>'
    schema = [{"@type": "WebPage", "@id": f"{S.BASE}{url}#webpage", "url": S.BASE + url, "name": h1, "isPartOf": {"@id": S.SITE_ID},
               "publisher": {"@id": S.ORG_ID}, "dateModified": S.TODAY_ISO, "inLanguage": "en-US"}]
    S.page(url, title, meta, hero, body, crumbs=crumbs, schema=schema, priority=0.3, kind="legal")


def build_legal():
    B, O, P, D = S.BRAND, S.OWNER, S.PHONE_DISPLAY, S.DOMAIN

    _legal("/disclaimer/", "Disclaimer", f"Disclaimer | Referral Service Disclosure | {B}",
           f"{B} disclaimer: how our pest control referral service works, who performs the work, call recording and compensation disclosure.",
           f"Document: Service and referral disclaimer for {D}, operated by {O}.", f'''
<h2>1. {B} is a referral and scheduling service</h2>
<p>{B} operates this website and the phone number {P} to help people reach pest control providers. {B} is not a pest control company and does not inspect, treat, apply pesticides, set traps, remove wildlife, repair structures or perform any other pest control work.</p>
<h2>2. Who performs the work</h2>
<p>Calls and requests are connected to independent pest control providers who participate in our network. Those providers are separate businesses. They are solely responsible for holding the licenses, certifications and insurance their state requires; for their inspections, recommendations, pricing, contracts, warranties and workmanship; and for complying with pesticide labels and laws. Any agreement for service is between you and the provider.</p>
<h2>3. Compensation</h2>
<p>{B} may be paid by providers or marketing partners when a call or request is connected. This compensation may influence which provider receives your call. It does not change the price the provider quotes to you.</p>
<h2>4. Call recording</h2>
<p>Calls to {P} may be recorded and monitored for quality, training and dispute resolution. Some states, including California, Florida, Illinois, Maryland, Massachusetts, Montana, New Hampshire, Pennsylvania and Washington, require the consent of all parties to record a call. By staying on the line after the recording notice, you consent to recording. If you do not consent, please end the call and use the <a href="/contact/">contact form</a>.</p>
<h2>5. No guarantee of availability</h2>
<p>Provider availability varies by location, season and pest. {B} does not guarantee that a provider will be available in your area, at a particular time, or for a particular service.</p>
<h2>6. Information is general, not professional advice</h2>
<p>Content on this website is general information about pests and pest control. It is not legal, medical, financial or professional pest control advice, and it does not replace an inspection by a licensed professional. For medical concerns such as stings, bites, rodent exposure or pesticide exposure, contact a doctor, call 911 in an emergency, or call Poison Control at 1-800-222-1222.</p>
<h2>7. No endorsement</h2>
<p>References to government agencies, universities, standards bodies or products are for information only and do not imply endorsement of {B} by those organizations.</p>
<h2>8. Contact</h2>
<p>Questions about this disclaimer can be sent through the <a href="/contact/">contact page</a>.</p>''')

    _legal("/editorial-policy/", "Editorial Policy", f"Editorial Policy | How {B} Content Is Written",
           f"How {B} researches, writes, fact-checks and updates its pest control guides, what we never do, and how to report an error.",
           f"Document: Editorial standards and review process for content published on {D}.", f'''
<h2>Who writes our content</h2>
<p>Pages on {D} are written and edited by the {B} content team under the direction of {O}. Our goal is to explain pest problems and professional treatment options in plain language so readers can make informed decisions and ask better questions when a provider visits.</p>
<h2>How we research</h2>
<ul><li>We rely on primary sources: the U.S. Environmental Protection Agency, the Centers for Disease Control and Prevention, the National Pesticide Information Center, state pest control regulators and land-grant university extension programs.</li><li>Service pages list their sources in a Sources section with links.</li><li>Search and keyword data guide which questions we answer, never what the answer says.</li></ul>
<h2>Fact-checking and review</h2>
<p>Every service page is checked against its cited sources before publishing. Pages show a "Last reviewed" date and are reviewed at least once a year, and sooner when regulations, products or public health guidance change.</p>
<h2>What we don't do</h2>
<ul><li>We don't publish fake reviews, ratings or testimonials.</li><li>We don't claim licenses, certifications, awards, response times or business history that cannot be verified.</li><li>We don't publish prices we cannot support with current data; we explain what affects cost instead.</li><li>We don't give medical or legal advice.</li></ul>
<h2>Referral disclosure</h2>
<p>{B} is a referral and scheduling service and may be compensated when calls are connected to providers. Editorial content is written to inform readers, not to favor any provider. See the <a href="/disclaimer/">disclaimer</a>.</p>
<h2>Corrections</h2>
<p>If you find an error or outdated information, please tell us through the <a href="/contact/">contact page</a> with the page address and the issue. We review reports promptly and update pages when a correction is warranted.</p>''')

    _legal("/privacy-policy/", "Privacy Policy", f"Privacy Policy | {B}",
           f"{B} privacy policy: what we collect from calls and forms, how it is shared with pest control providers, and your privacy rights by state.",
           f"Document: Privacy policy for {D} and calls to {P}. Operator and data controller: {O}.", f'''
<h2>1. Who we are</h2>
<p>This website, {D}, and the phone number {P} are operated by {O} under the name {B}. This policy explains what information we collect, how we use and share it, and the choices you have.</p>
<h2>2. Information we collect</h2>
<ul><li><strong>Information you give us:</strong> name, phone number, ZIP code, state, the service you need and any message you send through our forms.</li><li><strong>Call information:</strong> your phone number, call time and duration, the area code and approximate location, and, where you consent, call recordings.</li><li><strong>Device and usage data:</strong> pages viewed, referring pages, browser and device type, collected through privacy-focused, cookie-free analytics and standard server logs.</li></ul>
<h2>3. How we use information</h2>
<ul><li>To connect you with a pest control provider who serves your area and to pass along your request</li><li>To follow up about your request</li><li>To measure call quality, prevent fraud and improve this website</li><li>To comply with legal obligations</li></ul>
<h2>4. How we share information</h2>
<p>We share your request details with the independent pest control provider, and where applicable a call-routing or marketing partner, so they can respond to you. We may share information with service providers who host our website, route calls and deliver email, under contracts that limit their use of it. We may disclose information when required by law or to protect rights and safety. We do not sell personal information for money. Sharing a request with a provider so it can contact you may be considered a "sale" or "sharing" under some state laws; you can opt out as described below.</p>
<h2>5. Calls, texts and consent</h2>
<p>We follow the Telephone Consumer Protection Act and the Telemarketing Sales Rule. When you submit a form, you agree that we and a provider serving your area may contact you about your request at the number provided, including by call or text. Consent is not required to buy services. Reply STOP to any text to opt out. Calls may be recorded with notice; see the <a href="/disclaimer/">disclaimer</a> for all-party consent states.</p>
<h2>6. Cookies and analytics</h2>
<p>This site does not use advertising cookies. We use cookie-free analytics that do not track you across other websites. Your browser may store basic technical data needed for the site to work.</p>
<h2>7. Data retention and security</h2>
<p>We keep request and call records for as long as needed to provide the service, resolve disputes and meet legal obligations, generally no longer than 24 months, then delete or de-identify them. We use reasonable administrative, technical and physical safeguards. Every state has a data breach notification law, and we will notify affected people and regulators as those laws require.</p>
<h2>8. Your privacy rights</h2>
<p>Depending on where you live, laws such as the California Consumer Privacy Act as amended by the California Privacy Rights Act, and comprehensive privacy laws in states including Colorado, Connecticut, Virginia, Texas, Oregon and others, may give you the right to know, access, correct, delete or obtain a copy of your personal information, and to opt out of the sale or sharing of personal information or targeted advertising. Regardless of whether a specific law applies to us, we honor these requests from any U.S. resident. To make a request, use the <a href="/contact/">contact page</a> and choose "Other". We will verify your request using information you have already given us and will not discriminate against you for exercising your rights. You may use an authorized agent where state law allows.</p>
<h2>9. Children</h2>
<p>This website is not directed to children under 13, and we do not knowingly collect their personal information, consistent with the Children's Online Privacy Protection Act.</p>
<h2>10. Changes</h2>
<p>We may update this policy and will change the date at the top of the page when we do.</p>
<h2>11. Contact</h2>
<p>Privacy questions or requests: use the <a href="/contact/">contact page</a> or call {P}.</p>''')

    _legal("/terms/", "Terms of Use", f"Terms of Use | {B}",
           f"Terms of use for {D}: use of the {B} referral service, provider responsibilities, limits of liability and governing terms.",
           f"Document: Terms of use governing {D} and the {B} referral service, operated by {O}.", f'''
<h2>1. Acceptance</h2>
<p>By using {D} or calling {P}, you agree to these terms. If you do not agree, do not use the site or service.</p>
<h2>2. The service</h2>
<p>{B} is a free-to-use referral and scheduling service that connects people with independent pest control providers. {B} does not perform pest control work and is not a party to any agreement between you and a provider. See the <a href="/disclaimer/">disclaimer</a>.</p>
<h2>3. Your responsibilities</h2>
<ul><li>Provide accurate information when you call or submit a form.</li><li>Verify a provider's license, insurance and written estimate before authorizing work.</li><li>Do not misuse the site, submit false requests, scrape content or attempt to disrupt the service.</li></ul>
<h2>4. Provider responsibilities</h2>
<p>Providers are solely responsible for their licenses, insurance, compliance with pesticide labels and laws, pricing, contracts, guarantees and workmanship. Any dispute about work performed is between you and the provider.</p>
<h2>5. Content</h2>
<p>Site content is general information, not professional advice, and may change without notice. Text, graphics and the {B} name and logo belong to {B} or its licensors. Photos are used under their license terms.</p>
<h2>6. Disclaimer of warranties</h2>
<p>The site and service are provided "as is" without warranties of any kind, to the fullest extent permitted by law.</p>
<h2>7. Limitation of liability</h2>
<p>To the fullest extent permitted by law, {B} and {O} are not liable for indirect, incidental or consequential damages, or for any act or omission of a provider, arising from use of the site or service. Some states do not allow certain limitations, so these may not apply to you.</p>
<h2>8. Third-party links</h2>
<p>Links to government, university and other websites are provided for reference. We are not responsible for their content.</p>
<h2>9. Changes and governing terms</h2>
<p>We may update these terms by posting a new version with a new date. These terms are governed by applicable U.S. federal law and the laws of the state where the operator is located, without regard to conflict-of-law rules, except where your state's consumer protection laws provide otherwise.</p>
<h2>10. Contact</h2>
<p>Questions about these terms: <a href="/contact/">contact {B}</a>.</p>''')

    _legal("/accessibility/", "Accessibility Statement", f"Accessibility Statement | {B}",
           f"{B} is committed to an accessible website. Our WCAG 2.1 AA goals, accessibility features and how to report a barrier.",
           f"Document: Accessibility statement and conformance goals for {D}.", f'''
<h2>Our commitment</h2>
<p>{B} wants everyone, including people who use assistive technology, to be able to find pest control help. We aim to meet the Web Content Accessibility Guidelines (WCAG) 2.1 Level AA.</p>
<h2>Accessibility features</h2>
<ul><li>A skip link to jump to the main content</li><li>One main heading per page with headings in logical order</li><li>Text alternatives for informative images and hidden decorative graphics</li><li>Color contrast of at least 4.5:1 for body text</li><li>Keyboard-accessible navigation, menus and forms with visible focus styles</li><li>Labeled form fields and status messages announced to screen readers</li><li>Layouts that work from small phone screens to large monitors and at 200% zoom</li><li>Respect for reduced-motion settings</li></ul>
<h2>Phone access</h2>
<p>Every page offers the same service by phone at {P}. Callers who use relay services can dial 711 to reach the Telecommunications Relay Service.</p>
<h2>Known limitations</h2>
<p>Some linked third-party sites, such as government PDFs, may not meet the same standards. We link to them for reference and cannot change them.</p>
<h2>Report a barrier</h2>
<p>If something on this site is hard to use, tell us through the <a href="/contact/">contact page</a> with the page address and the problem. We review reports and work to fix issues promptly.</p>''')
