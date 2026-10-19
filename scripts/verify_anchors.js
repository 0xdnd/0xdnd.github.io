const fs = require('fs');

const html = fs.readFileSync('index.html', 'utf8');

// Find all id attributes in the HTML
const idRegex = /id="([^"]+)"/g;
const ids = new Set();
let match;
while ((match = idRegex.exec(html)) !== null) {
  ids.add(match[1]);
}

// Find all nav blocks
const navRegex = /<nav\b[^>]*>([\s\S]*?)<\/nav>/gi;
const navAnchors = [];
let navMatch;
while ((navMatch = navRegex.exec(html)) !== null) {
  const navContent = navMatch[1];
  const hrefRegex = /href="#([^"]+)"/g;
  let hrefMatch;
  while ((hrefMatch = hrefRegex.exec(navContent)) !== null) {
    navAnchors.push(hrefMatch[1]);
  }
}

console.log('--- NAV ANCHOR INTEGRITY AUDIT ---');
console.log(`Document IDs discovered: ${ids.size}`);
console.log(`Nav anchors discovered: ${navAnchors.length}`);

let failed = false;
for (const anchor of navAnchors) {
  const exists = ids.has(anchor);
  console.log(`Anchor: #${anchor} -> ${exists ? 'EXISTS (OK)' : 'MISSING TARGET (FAIL)'}`);
  if (!exists) {
    failed = true;
  }
}

// Also check ALL internal href="#..." anchors across the entire document
const allHrefRegex = /href="#([^"]+)"/g;
const allDocAnchors = [];
while ((match = allHrefRegex.exec(html)) !== null) {
  allDocAnchors.push(match[1]);
}
console.log(`\nTotal internal document anchors: ${allDocAnchors.length}`);
const missingDocAnchors = allDocAnchors.filter(a => !ids.has(a));
if (missingDocAnchors.length > 0) {
  console.error(`Missing anchor targets in document: ${missingDocAnchors.join(', ')}`);
  failed = true;
} else {
  console.log('All internal document anchors successfully resolve to valid target IDs.');
}

if (failed) {
  console.error('\nAUDIT RESULT: FAILED - Broken anchors detected.');
  process.exit(1);
} else {
  console.log('\nAUDIT RESULT: PASSED - 100% of internal anchors resolve cleanly.');
}
