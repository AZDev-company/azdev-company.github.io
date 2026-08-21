/* ============================================================
   AZ DEV — site behaviour
   ============================================================ */
'use strict';

const I18N = {
  en: {
    'a11y.skip': 'Skip to content',
    'brand.sub': 'SOFTWARE DEVELOPMENT',
    'nav.services': 'Services', 'nav.work': 'Work', 'nav.stack': 'Stack',
    'nav.process': 'Process', 'nav.faq': 'FAQ', 'nav.contact': 'Contact',
    'nav.start': 'Start a project',

    'hero.eyebrow': 'PRODUCT ENGINEERING STUDIO',
    'hero.title': 'We build digital products that feel <em>built, not templated.</em>',
    'hero.body': 'From mobile apps to business platforms, AZ DEV brings product thinking, interface design and engineering into a single delivery path — so what ships actually works.',
    'hero.work': 'See our work', 'hero.talk': 'Start a conversation',
    'hero.f1v': 'iOS · Android · Web', 'hero.f1k': 'Platforms we ship on',
    'hero.f2v': 'Arabic & English', 'hero.f2k': 'Full RTL support',
    'hero.f3v': 'Design → Launch', 'hero.f3k': 'One accountable team',

    'services.title': 'Built around the product.',
    'services.body': "We don't sell isolated screens. We build the product system around the business goal — and stay accountable for it after launch.",
    'svc1.t': 'Mobile applications', 'svc1.d': 'iOS and Android apps with polished interactions, scalable architecture and store-ready release pipelines.',
    'svc2.t': 'Web & dashboards', 'svc2.d': 'Responsive platforms and operations dashboards that make complex business workflows easier to run every day.',
    'svc3.t': 'Custom software', 'svc3.d': 'Purpose-built systems, integrations and automation for teams that need software to fit how they actually work.',
    'svc4.t': 'UI / UX design', 'svc4.d': 'User journeys and design systems that make a product feel clear, modern and deliberate in every detail.',

    'work.title': 'Selected product work.',
    'work.body': 'Concept-led showcases built in-house to demonstrate the depth of product AZ DEV designs and engineers — interface, data and operations together.',

    'stack.title': 'The stack behind the work.',
    'stack.body': 'Mature, well-supported technology chosen for maintainability — so the product stays cheap to change two years from now.',
    'stk1.t': 'Mobile', 'stk1.x': 'App Store & Play release',
    'stk2.t': 'Backend', 'stk3.t': 'Web', 'stk3.x': 'Responsive & RTL',
    'stk4.t': 'Data & maps', 'stk4.x': 'Reporting & dashboards',

    'process.title': 'One team. One delivery path.',
    'process.body': 'Strategy, design and engineering stay connected from the first conversation to release — no handover gaps for work to fall through.',
    'p1.t': 'Discover', 'p1.d': 'Understand the business, the users, the constraints and what success has to look like.',
    'p2.t': 'Design', 'p2.d': 'Shape the user journey, visual language and product system before a line of code is written.',
    'p3.t': 'Build', 'p3.d': 'Engineer the experience with clean architecture, real integrations and continuous quality checks.',
    'p4.t': 'Launch', 'p4.d': 'Ship to the stores, watch how it behaves, improve it, and keep it ready for what comes next.',
    'eng1.t': 'Fixed scope', 'eng1.d': 'A defined product for a defined price. Best when the requirements are already clear.',
    'eng2.t': 'Dedicated squad', 'eng2.d': 'A team working with you month to month, for products that keep evolving as they grow.',
    'eng3.t': 'Support & care', 'eng3.d': 'Maintenance, monitoring and release management after launch, so nothing goes quiet.',

    'faq.title': 'Questions worth asking.',
    'faq.body': 'The things clients ask before the first meeting — answered plainly, so the first call can be about your product instead.',
    'q1': 'How long does a first version usually take?',
    'a1': 'Most first releases land between two and four months, depending on how many user roles and integrations are involved. You get a scoped timeline after the discovery conversation, not before it.',
    'q2': 'Do you work with an existing codebase?',
    'a2': 'Yes. We start with a short technical review, tell you honestly what is worth keeping and what is not, and agree a plan before touching anything.',
    'q3': 'Who owns the code and the accounts?',
    'a3': 'You do — repository, store accounts, servers and design files are all in your name from the start. Nothing is held hostage.',
    'q4': 'Can you build Arabic-first products?',
    'a4': 'Yes. Arabic and English with proper right-to-left layout is a default here, not a translation bolted on at the end.',
    'q5': 'What happens after launch?',
    'a5': 'We stay on for monitoring, store releases and improvements. You can move to a lighter support agreement whenever the product is stable.',

    'contact.title': 'Have a product in mind?',
    'contact.body': "Tell us what you want to build. We'll turn the first conversation into a clear, costed next step — no obligation attached.",
    'contact.n1': 'We reply within one business day',
    'contact.n2': 'The first call is a scoping call, not a pitch',
    'contact.n3': 'You leave with a written summary either way',
    'contact.label': "LET'S BUILD IT TOGETHER",

    'footer.blurb': 'A product engineering studio for teams that want software built properly the first time.',
    'footer.explore': 'Explore', 'footer.build': 'We build',
    'footer.rights': 'All rights reserved.', 'footer.note': 'Built for ideas that deserve to ship.'
  },

  ar: {
    'a11y.skip': 'تخطَّ إلى المحتوى',
    'brand.sub': 'تطوير برمجيات',
    'nav.services': 'الخدمات', 'nav.work': 'أعمالنا', 'nav.stack': 'التقنيات',
    'nav.process': 'طريقة العمل', 'nav.faq': 'أسئلة شائعة', 'nav.contact': 'تواصل معنا',
    'nav.start': 'ابدأ مشروعك',

    'hero.eyebrow': 'استوديو هندسة المنتجات الرقمية',
    'hero.title': 'نبني منتجات رقمية تبدو <em>مصنوعة خصيصًا، لا قالبًا جاهزًا.</em>',
    'hero.body': 'من تطبيقات الموبايل إلى منصات الأعمال، نجمع التفكير في المنتج وتصميم الواجهات والهندسة في مسار تنفيذ واحد — حتى يعمل ما نُطلقه فعلًا.',
    'hero.work': 'استعرض أعمالنا', 'hero.talk': 'ابدأ محادثة',
    'hero.f1v': 'iOS · Android · ويب', 'hero.f1k': 'المنصات التي نطلق عليها',
    'hero.f2v': 'عربي وإنجليزي', 'hero.f2k': 'دعم كامل للاتجاه من اليمين',
    'hero.f3v': 'تصميم ← إطلاق', 'hero.f3k': 'فريق واحد مسؤول',

    'services.title': 'نبني حول المنتج.',
    'services.body': 'لا نبيع شاشات منفصلة. نبني منظومة المنتج حول هدف العمل الحقيقي، ونظل مسؤولين عنها بعد الإطلاق.',
    'svc1.t': 'تطبيقات الموبايل', 'svc1.d': 'تطبيقات iOS وAndroid بتفاعلات دقيقة ومعمارية قابلة للتوسع ومسار إصدار جاهز للمتاجر.',
    'svc2.t': 'الويب ولوحات التحكم', 'svc2.d': 'منصات متجاوبة ولوحات تشغيل تجعل إدارة العمليات المعقدة أسهل كل يوم.',
    'svc3.t': 'برمجيات مخصصة', 'svc3.d': 'أنظمة وتكاملات وأتمتة مصممة لتناسب طريقة عمل فريقك فعليًا، لا العكس.',
    'svc4.t': 'تصميم الواجهات UI/UX', 'svc4.d': 'رحلات مستخدم وأنظمة تصميم تجعل المنتج واضحًا وحديثًا ومقصودًا في كل تفصيلة.',

    'work.title': 'نماذج من أعمال المنتجات.',
    'work.body': 'نماذج مفاهيمية بنيناها داخليًا لتوضيح عمق المنتجات التي نصممها ونطوّرها — الواجهة والبيانات والتشغيل معًا.',

    'stack.title': 'التقنيات وراء العمل.',
    'stack.body': 'تقنيات ناضجة ومدعومة جيدًا اخترناها لسهولة الصيانة — حتى يظل تعديل المنتج رخيصًا بعد سنتين.',
    'stk1.t': 'الموبايل', 'stk1.x': 'النشر على App Store وPlay',
    'stk2.t': 'الخلفية Backend', 'stk3.t': 'الويب', 'stk3.x': 'متجاوب ويدعم RTL',
    'stk4.t': 'البيانات والخرائط', 'stk4.x': 'تقارير ولوحات بيانات',

    'process.title': 'فريق واحد. مسار تنفيذ واحد.',
    'process.body': 'الاستراتيجية والتصميم والهندسة تظل متصلة من أول محادثة حتى الإطلاق — بلا فجوات تسليم يضيع فيها العمل.',
    'p1.t': 'الاكتشاف', 'p1.d': 'نفهم البيزنس والمستخدمين والقيود وشكل النجاح المطلوب.',
    'p2.t': 'التصميم', 'p2.d': 'نبني رحلة المستخدم واللغة البصرية ونظام المنتج قبل كتابة أي كود.',
    'p3.t': 'التطوير', 'p3.d': 'ننفذ التجربة بمعمارية نظيفة وتكاملات حقيقية واختبارات جودة مستمرة.',
    'p4.t': 'الإطلاق', 'p4.d': 'ننشر على المتاجر ونراقب السلوك ونحسّن ونجهّز المنتج للمرحلة التالية.',
    'eng1.t': 'نطاق محدد', 'eng1.d': 'منتج محدد بسعر محدد. الأنسب حين تكون المتطلبات واضحة بالفعل.',
    'eng2.t': 'فريق مخصص', 'eng2.d': 'فريق يعمل معك شهريًا، للمنتجات التي تتطور باستمرار مع نموها.',
    'eng3.t': 'دعم ومتابعة', 'eng3.d': 'صيانة ومراقبة وإدارة إصدارات بعد الإطلاق، حتى لا يتوقف شيء فجأة.',

    'faq.title': 'أسئلة تستحق أن تُسأل.',
    'faq.body': 'ما يسأله العملاء قبل أول اجتماع — بإجابات مباشرة، حتى تكون المكالمة الأولى عن منتجك أنت.',
    'q1': 'كم يستغرق بناء النسخة الأولى عادةً؟',
    'a1': 'معظم الإصدارات الأولى تستغرق من شهرين إلى أربعة أشهر، حسب عدد أدوار المستخدمين والتكاملات المطلوبة. تحصل على جدول زمني محدد بعد جلسة الاكتشاف، وليس قبلها.',
    'q2': 'هل تعملون على كود موجود مسبقًا؟',
    'a2': 'نعم. نبدأ بمراجعة تقنية قصيرة، ونخبرك بصراحة بما يستحق الإبقاء عليه وما لا يستحق، ونتفق على خطة قبل تعديل أي شيء.',
    'q3': 'من يملك الكود والحسابات؟',
    'a3': 'أنت — المستودع وحسابات المتاجر والخوادم وملفات التصميم كلها باسمك من البداية. لا شيء محتجز لدينا.',
    'q4': 'هل يمكنكم بناء منتجات عربية أولًا؟',
    'a4': 'نعم. العربية والإنجليزية مع تخطيط سليم من اليمين لليسار هي الوضع الافتراضي لدينا، وليست ترجمة تُضاف في النهاية.',
    'q5': 'ماذا يحدث بعد الإطلاق؟',
    'a5': 'نستمر في المراقبة وإصدارات المتاجر والتحسينات. ويمكنك الانتقال إلى اتفاقية دعم أخف متى استقر المنتج.',

    'contact.title': 'عندك منتج في بالك؟',
    'contact.body': 'احكِ لنا ما تريد بناءه، ونحوّل أول محادثة إلى خطوة تالية واضحة ومسعّرة — بلا أي التزام.',
    'contact.n1': 'نرد خلال يوم عمل واحد',
    'contact.n2': 'المكالمة الأولى لتحديد النطاق، وليست عرضًا تسويقيًا',
    'contact.n3': 'تخرج منها بملخص مكتوب في كل الأحوال',
    'contact.label': 'لنبنِه معًا',

    'footer.blurb': 'استوديو هندسة منتجات للفرق التي تريد برمجيات مبنية بشكل صحيح من المرة الأولى.',
    'footer.explore': 'تصفح', 'footer.build': 'ما نبنيه',
    'footer.rights': 'جميع الحقوق محفوظة.', 'footer.note': 'نبني أفكارًا تستحق أن ترى النور.'
  }
};

const $ = (s, r = document) => r.querySelector(s);
const $$ = (s, r = document) => [...r.querySelectorAll(s)];

let lang = localStorage.getItem('azdev-lang') || 'en';
let theme = localStorage.getItem('azdev-theme') || 'dark';
let PROJECTS = [];

/* ---------- theme ---------- */
function applyTheme() {
  document.documentElement.dataset.theme = theme;
  $('#themeBtn').firstElementChild.textContent = theme === 'dark' ? '☀' : '◐';
  const meta = document.querySelector('meta[name=theme-color]');
  if (meta) meta.content = theme === 'dark' ? '#060910' : '#F7F9FC';
}

/* ---------- i18n ---------- */
function applyLang() {
  const dict = I18N[lang];
  document.documentElement.lang = lang;
  document.documentElement.dir = lang === 'ar' ? 'rtl' : 'ltr';
  document.body.classList.toggle('rtl', lang === 'ar');
  $$('[data-i18n]').forEach(el => {
    const v = dict[el.dataset.i18n];
    if (v != null) el.innerHTML = v;
  });
  const b = $('#langBtn');
  b.textContent = lang === 'ar' ? 'EN' : 'عربي';
  b.setAttribute('aria-label', lang === 'ar' ? 'Switch to English' : 'التبديل إلى العربية');
  renderProjects();
}

/* ---------- projects ---------- */
function renderProjects() {
  const host = $('#projects');
  if (!host || !PROJECTS.length) return;
  host.innerHTML = PROJECTS.map((p, i) => {
    const n = String(i + 1).padStart(2, '0');
    const feats = (p.features || []).map(f =>
      `<div><b>${f.b[lang]}</b><span>${f.s[lang]}</span></div>`).join('');
    const tags = (p.tags || []).map(t => `<span class="tag">${t}</span>`).join('');
    return `<article class="case reveal" style="--accent:${p.accent}">
      <div class="case-copy">
        <p class="case-kicker">${n} — ${p.kicker[lang]}</p>
        <h3>${p.title[lang]}</h3>
        <p class="sub">${p.description[lang]}</p>
        <div class="tags">${tags}</div>
        <div class="case-features">${feats}</div>
      </div>
      <div class="case-visual">
        <img src="${p.image}" alt="${p.title[lang]} — interface showcase" loading="lazy" decoding="async" width="1200" height="760">
      </div>
    </article>`;
  }).join('');
  observe();
}

/* ---------- data ---------- */
async function load() {
  try {
    const [pr, sr] = await Promise.all([fetch('data/projects.json'), fetch('data/site.json')]);
    PROJECTS = await pr.json();
    const site = await sr.json();
    const mail = `https://mail.google.com/mail/?view=cm&fs=1&to=${encodeURIComponent(site.contact.email)}`;

    const e = $('#emailLink');
    e.href = mail; e.target = '_blank'; e.rel = 'noopener'; e.textContent = site.contact.email;
    $('#phoneLink').href = `tel:${site.contact.phone}`;
    $('#phoneLink').textContent = site.contact.phone;
    $('#instagramLink').href = site.social.instagram;
    $('#facebookLink').href = site.social.facebook;

    $('#footerEmail').href = mail;
    $('#footerEmail').target = '_blank';
    $('#footerEmail').rel = 'noopener';
    $('#footerEmail').textContent = site.contact.email;
    $('#footerPhone').href = `tel:${site.contact.phone}`;
    $('#footerPhone').textContent = site.contact.phone;
    $('#footerInstagram').href = site.social.instagram;
    $('#footerFacebook').href = site.social.facebook;

    renderProjects();
  } catch (err) {
    console.error('AZ DEV: could not load site data —', err);
  }
}

/* ---------- reveal ---------- */
let io;
function observe() {
  if (!('IntersectionObserver' in window)) {
    $$('.reveal').forEach(el => el.classList.add('visible'));
    return;
  }
  io = io || new IntersectionObserver(entries => {
    entries.forEach(en => {
      if (en.isIntersecting) { en.target.classList.add('visible'); io.unobserve(en.target); }
    });
  }, { threshold: .12, rootMargin: '0px 0px -40px 0px' });
  $$('.reveal:not(.visible)').forEach(el => io.observe(el));
}

/* ---------- mobile drawer ---------- */
const menuBtn = $('#menuBtn');
const drawer = $('#mobileMenu');
function setMenu(open) {
  menuBtn.setAttribute('aria-expanded', String(open));
  drawer.hidden = !open;
  document.body.style.overflow = open ? 'hidden' : '';
  menuBtn.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
}
menuBtn.addEventListener('click', () => setMenu(drawer.hidden));
drawer.addEventListener('click', e => { if (e.target.closest('a')) setMenu(false); });
document.addEventListener('keydown', e => { if (e.key === 'Escape' && !drawer.hidden) setMenu(false); });
addEventListener('resize', () => { if (innerWidth > 1060 && !drawer.hidden) setMenu(false); });

/* ---------- controls ---------- */
$('#themeBtn').addEventListener('click', () => {
  theme = theme === 'dark' ? 'light' : 'dark';
  localStorage.setItem('azdev-theme', theme);
  applyTheme();
});
$('#langBtn').addEventListener('click', () => {
  lang = lang === 'en' ? 'ar' : 'en';
  localStorage.setItem('azdev-lang', lang);
  applyLang();
});

/* ---------- scroll ---------- */
const nav = $('#siteNav');
const bar = $('.scroll-progress');
let ticking = false;
addEventListener('scroll', () => {
  if (ticking) return;
  ticking = true;
  requestAnimationFrame(() => {
    const max = document.documentElement.scrollHeight - innerHeight;
    bar.style.width = max > 0 ? `${Math.min(100, (scrollY / max) * 100)}%` : '0%';
    nav.classList.toggle('stuck', scrollY > 8);
    ticking = false;
  });
}, { passive: true });

/* ---------- boot ---------- */
$('#year').textContent = new Date().getFullYear();
applyTheme();
applyLang();
load();
observe();
