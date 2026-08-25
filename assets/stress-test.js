/* open-source.sgit.ai — the Change-of-Control Stress Test.
   Entirely client-side: nothing is sent anywhere, there is no server to send it to.
   Answers persist in localStorage so the page remembers a half-finished assessment,
   and every read/write is guarded because a private window, cleared site data, or a
   browser set to block storage makes the accessor itself throw. If storage is
   unavailable the tool still works for the length of the visit. */
(function () {
  'use strict';
  var LEGS = [
    { n: 1, name: 'Copyright structure',
      pass: 'DCO / inbound=outbound, copyright distributed',
      fail: 'Single-entity CLA aggregating contributor copyright',
      unclear: 'Not determinable from public artefacts' },
    { n: 2, name: 'Trademark holder',
      pass: 'Neutral foundation, charter-level transfer restrictions',
      fail: 'Held by the operating company',
      unclear: 'No published trademark policy' },
    { n: 3, name: 'Schema licence',
      pass: 'CC0 or CC BY, licensed separately from the code',
      fail: 'Undeclared, or bundled with the code licence',
      unclear: 'Could not establish what governs the schemas' },
    { n: 4, name: 'Fork capacity',
      pass: 'A named party with the headcount and mandate',
      fail: '"The community would fork it", with no named party',
      unclear: 'Candidates, but none with a stated mandate' }
  ];
  var KEY = 'os-sgit-stress-test-v1';
  var form = document.getElementById('legs');
  if (!form) return;
  var subject = document.getElementById('subject');
  var verdict = document.getElementById('verdict');
  var copied = document.getElementById('copied');

  function load() {
    try {
      var raw = window.localStorage.getItem(KEY);
      return raw ? JSON.parse(raw) : {};
    } catch (e) { return {}; }
  }
  function save(state) {
    try { window.localStorage.setItem(KEY, JSON.stringify(state)); } catch (e) { /* no storage */ }
  }
  function drop() {
    try { window.localStorage.removeItem(KEY); } catch (e) { /* no storage */ }
  }

  function read() {
    var state = { subject: subject.value };
    LEGS.forEach(function (leg) {
      var picked = form.querySelector('input[name="leg' + leg.n + '"]:checked');
      state['leg' + leg.n] = picked ? picked.value : '';
    });
    return state;
  }

  function answers(state) {
    return LEGS.map(function (leg) { return state['leg' + leg.n] || ''; });
  }

  function verdictFor(a) {
    var fails = a.filter(function (v) { return v === 'fail'; }).length;
    var unclear = a.filter(function (v) { return v === 'unclear'; }).length;
    var passes = a.filter(function (v) { return v === 'pass'; }).length;
    if (unclear >= 2) {
      return { cls: 'v-opaque', label: 'Opaque',
        line: 'Two or more legs could not be answered from public artefacts. For a project ' +
              'whose proposition is openness, that opacity is itself the finding — and it is ' +
              'the one finding you can report without any further research.' };
    }
    if (fails === 0 && passes === 4) {
      return { cls: 'v-strong', label: 'Structurally survivable',
        line: 'No single party holds the standing to change the terms, the name is held ' +
              'neutrally, the schemas are separately and openly licensed, and you can name ' +
              'who would run the fork. This is the structure the argument says to look for.' };
    }
    if (fails >= 3) {
      return { cls: 'v-weak', label: 'Single-party dependent',
        line: 'This is the pattern every catalogued relicensing between 2018 and 2024 ' +
              'followed. It does not mean the project will be relicensed — it means nothing ' +
              'structural would stop it, and that acquisition would carry the standing with it.' };
    }
    return { cls: 'v-mixed', label: 'Mixed exposure',
      line: 'Some legs hold and some do not. Read the failing legs as a description of the ' +
            'specific exposure you are carrying, and decide whether it is priced correctly ' +
            'for what this dependency actually does for you.' };
  }

  function render() {
    var state = read();
    var a = answers(state);
    LEGS.forEach(function (leg, i) {
      var li = form.querySelector('.leg[data-leg="' + leg.n + '"]');
      li.className = 'leg' + (a[i] ? ' answered-' + a[i] : '');
    });
    if (a.some(function (v) { return !v; })) {
      var done = a.filter(Boolean).length;
      verdict.innerHTML = '<p class="verdict-empty">' + done + ' of 4 legs answered. '
        + 'Answer the rest to see the verdict.</p>';
      save(state);
      return;
    }
    var v = verdictFor(a);
    var name = state.subject.trim();
    var rows = LEGS.map(function (leg, i) {
      var cls = a[i] === 'pass' ? 'opt-yes' : (a[i] === 'fail' ? 'opt-no' : 'opt-part');
      var word = a[i] === 'pass' ? 'Passes' : (a[i] === 'fail' ? 'Fails' : 'Unclear');
      return '<li><b>Leg ' + leg.n + ' · ' + esc(leg.name) + '</b> — '
        + '<span class="opt-verdict ' + cls + '">' + word + '</span> '
        + esc(leg[a[i]]) + '</li>';
    }).join('');
    verdict.innerHTML =
      '<div class="vhead"><span class="vpill ' + v.cls + '">' + v.label + '</span>'
      + (name ? '<b>' + esc(name) + '</b>' : '') + '</div>'
      + '<p>' + v.line + '</p><ul>' + rows + '</ul>'
      + '<p class="small dim">A verdict is a description of exposure, not a recommendation. '
      + 'Plenty of software worth using fails legs one and two.</p>';
    save(state);
  }

  function esc(s) {
    return String(s).replace(/[&<>"]/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c];
    });
  }

  function markdown() {
    var state = read();
    var a = answers(state);
    var name = state.subject.trim() || 'Unnamed project';
    var out = ['# Change-of-Control Stress Test — ' + name, ''];
    if (a.every(Boolean)) {
      var v = verdictFor(a);
      out.push('**Verdict: ' + v.label + '**', '', v.line, '');
    }
    out.push('| Leg | Result | Basis |', '|---|---|---|');
    LEGS.forEach(function (leg, i) {
      var word = a[i] === 'pass' ? 'Passes' : (a[i] === 'fail' ? 'Fails'
        : (a[i] === 'unclear' ? 'Unclear' : '—'));
      out.push('| ' + leg.n + '. ' + leg.name + ' | ' + word + ' | '
        + (a[i] ? leg[a[i]] : 'not answered') + ' |');
    });
    out.push('', 'Run with the test published at https://open-source.sgit.ai/survivability/stress-test.html',
      '(CC BY 4.0). The four legs are answerable from public artefacts.');
    return out.join('\n');
  }

  form.addEventListener('change', render);
  subject.addEventListener('input', render);

  document.getElementById('copy').addEventListener('click', function () {
    var text = markdown();
    var done = function () {
      copied.hidden = false;
      window.setTimeout(function () { copied.hidden = true; }, 2500);
    };
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).then(done, function () { fallback(text, done); });
    } else {
      fallback(text, done);
    }
  });

  /* execCommand('copy') is deprecated but it is the only path left when the async
     clipboard API is unavailable or refused, which happens in more browsers than
     the spec suggests. Losing the copy button entirely is the worse outcome. */
  function fallback(text, done) {
    var ta = document.createElement('textarea');
    ta.value = text;
    ta.setAttribute('readonly', '');
    ta.style.position = 'fixed';
    ta.style.opacity = '0';
    document.body.appendChild(ta);
    ta.select();
    try { document.execCommand('copy'); done(); } catch (e) { /* nothing left to try */ }
    document.body.removeChild(ta);
  }

  document.getElementById('clear').addEventListener('click', function () {
    form.querySelectorAll('input[type=radio]').forEach(function (r) { r.checked = false; });
    subject.value = '';
    drop();
    render();
  });

  /* Restore a half-finished assessment, then draw. */
  (function restore() {
    var state = load();
    if (state && typeof state === 'object') {
      if (typeof state.subject === 'string') subject.value = state.subject;
      LEGS.forEach(function (leg) {
        var v = state['leg' + leg.n];
        if (!v) return;
        var input = form.querySelector('input[name="leg' + leg.n + '"][value="' + v + '"]');
        if (input) input.checked = true;
      });
    }
    render();
  }());
}());
