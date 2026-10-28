/**
 * STUDYROOM — Class XII NEB Dashain Homework 2083
 * Core Application Controller
 */

(function () {
  'use strict';

  // State Management
  let currentSubjectId = null;
  let allSearchItems = [];

  // DOM Elements
  const subjectNavList = document.getElementById('subject-nav-list');
  const contentContainer = document.getElementById('content-container');
  const themeToggle = document.getElementById('theme-toggle');
  const brandLink = document.getElementById('brand-link');
  const sidebar = document.getElementById('sidebar');
  const menuBtn = document.getElementById('menu-btn');
  const drawerOverlay = document.getElementById('drawer-overlay');
  const backToTopBtn = document.getElementById('back-to-top');
  const printBtn = document.getElementById('print-btn');
  const printSubjectName = document.getElementById('print-subject-name');
  
  // Search Modal Elements
  const searchTrigger = document.getElementById('search-trigger');
  const searchModal = document.getElementById('search-modal');
  const searchBackdrop = document.getElementById('search-backdrop');
  const searchInput = document.getElementById('search-input');
  const searchClearBtn = document.getElementById('search-clear-btn');
  const searchResultsContainer = document.getElementById('search-results-container');
  const toastContainer = document.getElementById('toast-container');

  // Initialize Application
  function init() {
    initTheme();
    buildSearchIndex();
    renderSidebarNav();
    bindEvents();
    handleInitialRoute();
    if (window.lucide) {
      window.lucide.createIcons();
    }
  }

  // Calculate Total Questions for a subject
  function getSubjectQuestionCount(subject) {
    if (!subject || !subject.sections) return 0;
    return subject.sections.reduce((total, section) => total + (section.questions ? section.questions.length : 0), 0);
  }

  // Theme Management
  function initTheme() {
    const savedTheme = localStorage.getItem('studyroom_theme') || 'dark';
    document.documentElement.setAttribute('data-theme', savedTheme);
  }

  function toggleTheme() {
    const currentTheme = document.documentElement.getAttribute('data-theme') || 'dark';
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', newTheme);
    localStorage.setItem('studyroom_theme', newTheme);
    showToast(`Switched to ${newTheme} mode`);
  }

  // Build Full-Text Search Index
  function buildSearchIndex() {
    allSearchItems = [];
    if (!window.HOMEWORK_DATA) return;

    window.HOMEWORK_DATA.forEach(subject => {
      subject.sections.forEach(section => {
        section.questions.forEach(q => {
          allSearchItems.push({
            subjectId: subject.id,
            subjectTitle: subject.title,
            sectionName: section.name,
            questionId: q.id,
            questionNumber: q.number,
            questionText: q.question,
            answerText: q.answer
          });
        });
      });
    });
  }

  // Render Sidebar Subject Navigation
  function renderSidebarNav() {
    if (!window.HOMEWORK_DATA) return;
    subjectNavList.innerHTML = '';

    window.HOMEWORK_DATA.forEach(subject => {
      const qCount = getSubjectQuestionCount(subject);
      const li = document.createElement('li');

      const btn = document.createElement('button');
      btn.className = `nav-item-btn ${currentSubjectId === subject.id ? 'active' : ''}`;
      btn.dataset.subjectId = subject.id;
      btn.innerHTML = `
        <div class="nav-item-left">
          <i data-lucide="${subject.icon || 'book'}" class="nav-icon"></i>
          <span>${subject.title}</span>
        </div>
        <span class="nav-badge">${qCount}</span>
      `;

      btn.addEventListener('click', () => {
        navigateToSubject(subject.id);
        closeMobileSidebar();
      });

      li.appendChild(btn);
      subjectNavList.appendChild(li);
    });

    if (window.lucide) {
      window.lucide.createIcons();
    }
  }

  // Update Active State in Navigation
  function updateNavActiveState() {
    const navButtons = document.querySelectorAll('.nav-item-btn');
    navButtons.forEach(btn => {
      if (btn.dataset.subjectId === currentSubjectId) {
        btn.classList.add('active');
      } else {
        btn.classList.remove('active');
      }
    });
  }

  // Markdown & LaTeX Parsing
  function formatMarkdown(content) {
    if (!content) return '';

    // Handle code blocks (e.g. ```c ... ```)
    let formatted = content.replace(/```([a-zA-Z]*)\n([\s\S]*?)```/g, (match, lang, code) => {
      const language = lang.trim() || 'code';
      const cleanCode = escapeHtml(code.trim());
      return `
        <div class="code-wrapper">
          <div class="code-header">
            <span>${language.toUpperCase()}</span>
            <button class="copy-code-btn" data-code="${escapeAttribute(code.trim())}">
              <i data-lucide="copy"></i>
              <span>Copy Code</span>
            </button>
          </div>
          <pre><code>${cleanCode}</code></pre>
        </div>
      `;
    });

    // Handle Tables
    formatted = formatted.replace(/\n(\|.+?\|\n\|[-:\s|]+?\|\n(?:\|.+?\|\n?)+)/g, match => {
      const rows = match.trim().split('\n');
      if (rows.length < 2) return match;

      const headerCells = rows[0].split('|').filter(c => c.trim() !== '');
      let tableHtml = '<table><thead><tr>';
      headerCells.forEach(cell => {
        tableHtml += `<th>${cell.trim()}</th>`;
      });
      tableHtml += '</tr></thead><tbody>';

      for (let i = 2; i < rows.length; i++) {
        const bodyCells = rows[i].split('|').filter(c => c.trim() !== '');
        tableHtml += '<tr>';
        bodyCells.forEach(cell => {
          tableHtml += `<td>${cell.trim()}</td>`;
        });
        tableHtml += '</tr>';
      }
      tableHtml += '</tbody></table>';
      return tableHtml;
    });

    // Handle Headings (###)
    formatted = formatted.replace(/^### (.*$)/gim, '<h3>$1</h3>');
    formatted = formatted.replace(/^#### (.*$)/gim, '<h4>$1</h4>');

    // Handle Bold & Italic
    formatted = formatted.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
    formatted = formatted.replace(/\*(.*?)\*/g, '<em>$1</em>');

    // Handle Lists
    formatted = formatted.replace(/^\s*-\s+(.*$)/gim, '<li>$1</li>');
    formatted = formatted.replace(/(<li>.*<\/li>)/s, '<ul>$1</ul>');

    // Handle Paragraphs
    const paras = formatted.split(/\n\s*\n/);
    formatted = paras.map(p => {
      p = p.trim();
      if (!p) return '';
      if (p.startsWith('<h') || p.startsWith('<div') || p.startsWith('<table') || p.startsWith('<ul') || p.startsWith('<ol')) {
        return p;
      }
      return `<p>${p.replace(/\n/g, '<br>')}</p>`;
    }).join('\n');

    return formatted;
  }

  function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
  }

  function escapeAttribute(text) {
    return text.replace(/"/g, '&quot;').replace(/'/g, '&#39;');
  }

  // Render Landing Page / Homepage
  function renderLandingView() {
    currentSubjectId = null;
    updateNavActiveState();
    window.location.hash = '';

    let catalogCardsHtml = '';
    window.HOMEWORK_DATA.forEach(sub => {
      const count = getSubjectQuestionCount(sub);
      catalogCardsHtml += `
        <div class="subject-card" data-subject-id="${sub.id}">
          <div>
            <div class="card-top">
              <div class="card-icon">
                <i data-lucide="${sub.icon || 'book'}"></i>
              </div>
              <span class="card-badge">${count} Questions</span>
            </div>
            <h3 class="card-title">${sub.title}</h3>
            <p class="card-desc">${sub.description}</p>
          </div>
          <div class="card-footer">
            <span>Read Homework</span>
            <i data-lucide="arrow-right"></i>
          </div>
        </div>
      `;
    });

    contentContainer.innerHTML = `
      <div class="landing-view">
        <section class="hero-section hero-profile-section">
          <!-- Napra Creator Profile from https://linktr.ee/NapraB -->
          <div class="profile-card">
            <div class="profile-header">
              <div class="profile-avatar-wrapper">
                <img src="assets/avatar.jpg" alt="Napra" class="profile-avatar" onerror="this.src='https://ugc.production.linktr.ee/0c6089ca-1602-40b6-8ed5-73d94a627d8b_d3c73ac77580753336cc576fdc060de0-tplv-tiktokx-cropcenter-1080-1080.jpeg'">
                <span class="online-indicator" title="Active"></span>
              </div>
              <div class="profile-main">
                <div class="profile-title-row">
                  <h1 class="profile-name">Napra</h1>
                  <span class="profile-tag">🕷️🕸️</span>
                  <a href="https://linktr.ee/NapraB" target="_blank" rel="noopener noreferrer" class="profile-handle-badge">@NapraB</a>
                </div>
                <p class="profile-sub">Arpan Bhattarai · <strong>ARPN$</strong> · Artist, Creator & Developer</p>
                <div class="profile-badge-row">
                  <span class="badge-pill"><i data-lucide="music"></i> Artist & Producer</span>
                  <span class="badge-pill"><i data-lucide="code-2"></i> Developer</span>
                  <span class="badge-pill"><i data-lucide="map-pin"></i> Kathmandu, Nepal</span>
                </div>
              </div>
            </div>

            <!-- Social Links & Profiles Grid -->
            <div class="profile-socials-grid">
              <a href="https://linktr.ee/NapraB" target="_blank" rel="noopener noreferrer" class="social-chip chip-linktree">
                <i data-lucide="external-link"></i>
                <span>Linktree</span>
              </a>
              <a href="https://open.spotify.com/artist/0cGXlzy9d3D8IBrAsWTM9k?si=DkAy34XARBuqlxCESmuTZg" target="_blank" rel="noopener noreferrer" class="social-chip chip-spotify">
                <i data-lucide="disc"></i>
                <span>Spotify</span>
              </a>
              <a href="https://music.apple.com/us/artist/arpn%24/1877263805" target="_blank" rel="noopener noreferrer" class="social-chip chip-apple">
                <i data-lucide="music-2"></i>
                <span>Apple Music</span>
              </a>
              <a href="https://soundcloud.com/arpn-330192001" target="_blank" rel="noopener noreferrer" class="social-chip chip-soundcloud">
                <i data-lucide="radio"></i>
                <span>SoundCloud</span>
              </a>
              <a href="https://instagram.com/napra0_0" target="_blank" rel="noopener noreferrer" class="social-chip chip-instagram">
                <i data-lucide="instagram"></i>
                <span>Instagram</span>
              </a>
              <a href="https://tiktok.com/@napra.0_0" target="_blank" rel="noopener noreferrer" class="social-chip chip-tiktok">
                <i data-lucide="video"></i>
                <span>TikTok</span>
              </a>
              <a href="https://www.youtube.com/@Napra0_0" target="_blank" rel="noopener noreferrer" class="social-chip chip-youtube">
                <i data-lucide="youtube"></i>
                <span>YouTube</span>
              </a>
              <a href="https://github.com/Arpaann" target="_blank" rel="noopener noreferrer" class="social-chip chip-github">
                <i data-lucide="github"></i>
                <span>GitHub</span>
              </a>
              <a href="https://discord.gg/QAdnPr5T" target="_blank" rel="noopener noreferrer" class="social-chip chip-discord">
                <i data-lucide="message-circle"></i>
                <span>Discord</span>
              </a>
              <a href="https://www.twitch.tv/arpanbhattarai" target="_blank" rel="noopener noreferrer" class="social-chip chip-twitch">
                <i data-lucide="tv"></i>
                <span>Twitch</span>
              </a>
              <a href="https://www.linkedin.com/in/arpan-bhattarai-8b63ba370/" target="_blank" rel="noopener noreferrer" class="social-chip chip-linkedin">
                <i data-lucide="linkedin"></i>
                <span>LinkedIn</span>
              </a>
              <a href="https://www.pinterest.com/Arpn" target="_blank" rel="noopener noreferrer" class="social-chip chip-pinterest">
                <i data-lucide="image"></i>
                <span>Pinterest</span>
              </a>
            </div>

            <!-- Featured Releases & Social Highlights -->
            <div class="profile-highlights">
              <a href="https://open.spotify.com/track/5k54TSNACAVSC3yJ50tgqG?si=6c8a447c185b4e07" target="_blank" rel="noopener noreferrer" class="highlight-card">
                <div class="highlight-icon music-icon">
                  <i data-lucide="music"></i>
                </div>
                <div class="highlight-info">
                  <span class="highlight-title">shawty lil maddie</span>
                  <span class="highlight-desc">Latest Release on Spotify · ARPN$</span>
                </div>
                <i data-lucide="arrow-up-right" class="highlight-arrow"></i>
              </a>

              <a href="https://linktr.ee/pawsfinder0_0" target="_blank" rel="noopener noreferrer" class="highlight-card">
                <div class="highlight-icon pet-icon">
                  <i data-lucide="paw-print"></i>
                </div>
                <div class="highlight-info">
                  <span class="highlight-title">Pawsfinder0_0 : Socials</span>
                  <span class="highlight-desc">Lost Pet Recovery & Rescue Network</span>
                </div>
                <i data-lucide="arrow-up-right" class="highlight-arrow"></i>
              </a>
            </div>
          </div>

          <div class="hero-actions">
            <button class="btn btn-primary" id="start-reading-btn">
              <span>Explore Homework Answers</span>
              <i data-lucide="arrow-right"></i>
            </button>
          </div>
        </section>

        <section class="catalog-section">
          <h2 class="section-heading">Subject Directory</h2>
          <div class="subject-cards-grid">
            ${catalogCardsHtml}
          </div>
        </section>
      </div>
    `;

    document.getElementById('start-reading-btn').addEventListener('click', () => {
      if (window.HOMEWORK_DATA && window.HOMEWORK_DATA.length > 0) {
        navigateToSubject(window.HOMEWORK_DATA[0].id);
      }
    });

    const cards = contentContainer.querySelectorAll('.subject-card');
    cards.forEach(card => {
      card.addEventListener('click', () => {
        navigateToSubject(card.dataset.subjectId);
      });
    });

    window.scrollTo({ top: 0, behavior: 'smooth' });
    if (window.lucide) window.lucide.createIcons();
  }

  // Render Subject Reading View
  function renderSubjectView(subjectId, scrollToQuestionId = null) {
    const subject = window.HOMEWORK_DATA.find(s => s.id === subjectId);
    if (!subject) {
      renderLandingView();
      return;
    }

    currentSubjectId = subjectId;
    updateNavActiveState();
    printSubjectName.textContent = `Subject: ${subject.title}`;

    const totalQuestions = getSubjectQuestionCount(subject);

    // Build TOC Pills
    let tocPillsHtml = '';
    subject.sections.forEach(sec => {
      sec.questions.forEach(q => {
        const label = sec.questions.length > 30 ? `Q${q.number}` : `${q.number}`;
        tocPillsHtml += `
          <a href="#${subject.id}-${q.id}" class="toc-pill" data-target="${q.id}" title="${escapeAttribute(q.question.substring(0, 80))}">
            ${label}
          </a>
        `;
      });
    });

    // Build Content Sections
    let sectionsHtml = '';
    subject.sections.forEach(sec => {
      let questionsHtml = '';
      sec.questions.forEach(q => {
        const formattedAnswer = formatMarkdown(q.answer);

        questionsHtml += `
          <article class="qa-item" id="${q.id}">
            <div class="qa-header">
              <h2 class="question-text">Question ${q.number}. ${escapeHtml(q.question).replace(/\n/g, "<br>")}</h2>
              <div class="qa-actions">
                <button class="action-btn copy-qa-btn" title="Copy Question and Answer" data-qid="${q.id}">
                  <i data-lucide="copy"></i>
                </button>
                <button class="action-btn link-qa-btn" title="Copy Link to Question" data-qid="${q.id}">
                  <i data-lucide="link"></i>
                </button>
                <button class="action-btn share-qa-btn" title="Share Question" data-qid="${q.id}">
                  <i data-lucide="share-2"></i>
                </button>
              </div>
            </div>
            <div class="answer-body">
              <strong>Answer:</strong>
              ${formattedAnswer}
            </div>
          </article>
        `;
      });

      sectionsHtml += `
        <div class="sub-section-container">
          ${subject.sections.length > 1 ? `
            <div class="sub-section-header">
              <h2 class="sub-section-title">${sec.name}</h2>
              <span class="sub-section-count">(${sec.questions.length} Questions)</span>
            </div>
          ` : ''}
          ${questionsHtml}
        </div>
      `;
    });

    // Find Previous & Next Subjects for Pagination
    const currentIndex = window.HOMEWORK_DATA.findIndex(s => s.id === subjectId);
    const prevSubject = currentIndex > 0 ? window.HOMEWORK_DATA[currentIndex - 1] : null;
    const nextSubject = currentIndex < window.HOMEWORK_DATA.length - 1 ? window.HOMEWORK_DATA[currentIndex + 1] : null;

    contentContainer.innerHTML = `
      <div class="subject-view">
        <header class="subject-header">
          <div class="subject-title-row">
            <h1 class="subject-title">
              <i data-lucide="${subject.icon || 'book'}"></i>
              <span>${subject.title}</span>
            </h1>
            <span class="subject-count-pill">${totalQuestions} Questions</span>
          </div>
          <p class="subject-desc">${subject.description}</p>
        </header>

        <div class="toc-container">
          <span class="toc-title">QUESTION INDEX</span>
          <div class="toc-pills">
            ${tocPillsHtml}
          </div>
        </div>

        <div class="questions-container">
          ${sectionsHtml}
        </div>

        <div class="subject-pagination">
          ${prevSubject ? `
            <button class="pag-btn" id="prev-subject-btn" data-subject-id="${prevSubject.id}">
              <i data-lucide="chevron-left"></i>
              <span>${prevSubject.title}</span>
            </button>
          ` : '<div></div>'}

          ${nextSubject ? `
            <button class="pag-btn" id="next-subject-btn" data-subject-id="${nextSubject.id}">
              <span>${nextSubject.title}</span>
              <i data-lucide="chevron-right"></i>
            </button>
          ` : '<div></div>'}
        </div>
      </div>
    `;

    // Render LaTeX Math with KaTeX
    if (window.renderMathInElement) {
      window.renderMathInElement(contentContainer, {
        delimiters: [
          { left: '$$', right: '$$', display: true },
          { left: '$', right: '$', display: false }
        ],
        throwOnError: false
      });
    }

    // Attach Event Handlers for Code Copying, QA Copying, Sharing, Linking
    attachQAHandlers(subject);

    // Pagination Listeners
    const prevBtn = document.getElementById('prev-subject-btn');
    if (prevBtn) {
      prevBtn.addEventListener('click', () => navigateToSubject(prevBtn.dataset.subjectId));
    }
    const nextBtn = document.getElementById('next-subject-btn');
    if (nextBtn) {
      nextBtn.addEventListener('click', () => navigateToSubject(nextBtn.dataset.subjectId));
    }

    // Smooth scroll to requested question or top
    if (scrollToQuestionId) {
      setTimeout(() => {
        const el = document.getElementById(scrollToQuestionId);
        if (el) {
          el.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
      }, 100);
    } else {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    if (window.lucide) window.lucide.createIcons();
  }

  // Attach QA Action Handlers (Copy, Share, Link)
  function attachQAHandlers(subject) {
    // Copy Code Buttons
    contentContainer.querySelectorAll('.copy-code-btn').forEach(btn => {
      btn.addEventListener('click', e => {
        e.stopPropagation();
        const code = btn.getAttribute('data-code');
        navigator.clipboard.writeText(code).then(() => {
          showToast('Code copied to clipboard!');
        });
      });
    });

    // Copy Question & Answer
    contentContainer.querySelectorAll('.copy-qa-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        const qid = btn.dataset.qid;
        let foundQ = null;
        for (const sec of subject.sections) {
          const q = sec.questions.find(item => item.id === qid);
          if (q) { foundQ = q; break; }
        }

        if (foundQ) {
          const plainText = `Question ${foundQ.number}. ${foundQ.question}\n\nAnswer:\n${foundQ.answer}\n\n[Studyroom — Class XII NEB Dashain Homework 2083 by Arpan Bhattarai]`;
          navigator.clipboard.writeText(plainText).then(() => {
            showToast(`Question ${foundQ.number} copied to clipboard!`);
          });
        }
      });
    });

    // Copy Direct Link
    contentContainer.querySelectorAll('.link-qa-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        const qid = btn.dataset.qid;
        const link = `${window.location.origin}${window.location.pathname}#${subject.id}-${qid}`;
        window.history.pushState(null, null, `#${subject.id}-${qid}`);
        navigator.clipboard.writeText(link).then(() => {
          showToast('Direct link copied to clipboard!');
        });
      });
    });

    // Share Question
    contentContainer.querySelectorAll('.share-qa-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        const qid = btn.dataset.qid;
        const link = `${window.location.origin}${window.location.pathname}#${subject.id}-${qid}`;
        if (navigator.share) {
          navigator.share({
            title: `Studyroom — ${subject.title} Q${qid}`,
            text: `Check out this solution for ${subject.title} Class 12 NEB Homework`,
            url: link
          }).catch(() => {});
        } else {
          navigator.clipboard.writeText(link).then(() => {
            showToast('Link copied to clipboard (Sharing unsupported)');
          });
        }
      });
    });
  }

  // Navigation Logic
  function navigateToSubject(subjectId, questionId = null) {
    if (questionId) {
      window.location.hash = `${subjectId}-${questionId}`;
    } else {
      window.location.hash = subjectId;
    }
    renderSubjectView(subjectId, questionId);
  }

  function handleInitialRoute() {
    const hash = (window.location && window.location.hash) ? window.location.hash.replace('#', '').trim() : '';
    if (!hash) {
      renderLandingView();
      return;
    }

    if (!window.HOMEWORK_DATA) return;

    // Direct subject match (e.g., #computer-science)
    const exactSubject = window.HOMEWORK_DATA.find(s => s.id === hash);
    if (exactSubject) {
      renderSubjectView(exactSubject.id);
      return;
    }

    // Match subject prefix for question jump (e.g. #computer-science-cs-q1)
    for (const sub of window.HOMEWORK_DATA) {
      if (hash.startsWith(sub.id + '-')) {
        const questionId = hash.substring(sub.id.length + 1);
        renderSubjectView(sub.id, questionId);
        return;
      }
    }

    // Fallback
    renderLandingView();
  }

  // Mobile Drawer Helpers
  function openMobileSidebar() {
    sidebar.classList.add('open');
    drawerOverlay.classList.add('active');
  }

  function closeMobileSidebar() {
    sidebar.classList.remove('open');
    drawerOverlay.classList.remove('active');
  }

  // Search Engine Implementation
  function openSearchModal() {
    searchModal.classList.add('active');
    searchModal.setAttribute('aria-hidden', 'false');
    searchInput.value = '';
    searchClearBtn.style.display = 'none';
    searchResultsContainer.innerHTML = `
      <div class="search-empty-state">
        <i data-lucide="search" class="empty-icon"></i>
        <p>Type to search across all 7 subjects and 300+ questions & answers...</p>
      </div>
    `;
    setTimeout(() => searchInput.focus(), 50);
    if (window.lucide) window.lucide.createIcons();
  }

  function closeSearchModal() {
    searchModal.classList.remove('active');
    searchModal.setAttribute('aria-hidden', 'true');
    searchInput.blur();
  }

  function performSearch(query) {
    const trimmed = query.trim();
    if (!trimmed) {
      searchClearBtn.style.display = 'none';
      searchResultsContainer.innerHTML = `
        <div class="search-empty-state">
          <i data-lucide="search" class="empty-icon"></i>
          <p>Type to search across all 7 subjects and 300+ questions & answers...</p>
        </div>
      `;
      if (window.lucide) window.lucide.createIcons();
      return;
    }

    searchClearBtn.style.display = 'flex';
    const lower = trimmed.toLowerCase();
    const results = [];

    allSearchItems.forEach(item => {
      const qLower = item.questionText.toLowerCase();
      const aLower = item.answerText.toLowerCase();

      const qMatch = qLower.includes(lower);
      const aMatch = aLower.includes(lower);

      if (qMatch || aMatch) {
        // Excerpt generation around match
        let excerpt = '';
        if (aMatch) {
          const idx = aLower.indexOf(lower);
          const start = Math.max(0, idx - 40);
          const end = Math.min(item.answerText.length, idx + lower.length + 60);
          excerpt = (start > 0 ? '...' : '') + item.answerText.substring(start, end) + (end < item.answerText.length ? '...' : '');
        } else {
          excerpt = item.answerText.substring(0, 100) + '...';
        }

        results.push({
          item,
          excerpt,
          score: (qMatch ? 10 : 0) + (aMatch ? 5 : 0)
        });
      }
    });

    results.sort((a, b) => b.score - a.score);

    if (results.length === 0) {
      searchResultsContainer.innerHTML = `
        <div class="search-empty-state">
          <i data-lucide="alert-circle" class="empty-icon"></i>
          <p>No answers found matching "<strong>${escapeHtml(trimmed)}</strong>".</p>
        </div>
      `;
      if (window.lucide) window.lucide.createIcons();
      return;
    }

    let resultsHtml = '';
    results.slice(0, 25).forEach(res => {
      const highlightedQuestion = highlightText(res.item.questionText, trimmed);
      const highlightedExcerpt = highlightText(res.excerpt, trimmed);

      resultsHtml += `
        <div class="search-result-item" data-subject-id="${res.item.subjectId}" data-question-id="${res.item.questionId}">
          <div class="result-meta">
            <span>${res.item.subjectTitle}</span>
            <span>·</span>
            <span>${res.item.sectionName} (Q${res.item.questionNumber})</span>
          </div>
          <div class="result-question">${highlightedQuestion}</div>
          <div class="result-excerpt">${highlightedExcerpt}</div>
        </div>
      `;
    });

    searchResultsContainer.innerHTML = resultsHtml;

    // Attach click listeners to search results
    searchResultsContainer.querySelectorAll('.search-result-item').forEach(el => {
      el.addEventListener('click', () => {
        const subId = el.dataset.subjectId;
        const qId = el.dataset.questionId;
        closeSearchModal();
        navigateToSubject(subId, qId);
      });
    });

    if (window.lucide) window.lucide.createIcons();
  }

  function highlightText(text, query) {
    if (!text || !query) return escapeHtml(text || '');
    const clean = escapeHtml(text);
    const regex = new RegExp(`(${query.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')})`, 'gi');
    return clean.replace(regex, '<mark class="highlight">$1</mark>');
  }

  // Toast Notification
  function showToast(message) {
    const toast = document.createElement('div');
    toast.className = 'toast';
    toast.innerHTML = `
      <i data-lucide="check" style="width:16px;height:16px;color:var(--accent);"></i>
      <span>${escapeHtml(message)}</span>
    `;
    toastContainer.appendChild(toast);
    if (window.lucide) window.lucide.createIcons();

    setTimeout(() => {
      toast.style.opacity = '0';
      toast.style.transform = 'translateY(10px)';
      toast.style.transition = 'all 0.25s ease';
      setTimeout(() => toast.remove(), 250);
    }, 2500);
  }

  // Bind All Event Listeners
  function bindEvents() {
    // Theme Switcher
    themeToggle.addEventListener('click', toggleTheme);

    // Brand Link to Landing Page
    brandLink.addEventListener('click', e => {
      e.preventDefault();
      renderLandingView();
    });

    // Mobile Drawer
    menuBtn.addEventListener('click', openMobileSidebar);
    drawerOverlay.addEventListener('click', closeMobileSidebar);

    // Search Trigger
    searchTrigger.addEventListener('click', openSearchModal);
    searchBackdrop.addEventListener('click', closeSearchModal);

    // Search Input Typing
    let searchDebounce = null;
    searchInput.addEventListener('input', e => {
      clearTimeout(searchDebounce);
      searchDebounce = setTimeout(() => {
        performSearch(e.target.value);
      }, 150);
    });

    searchClearBtn.addEventListener('click', () => {
      searchInput.value = '';
      searchInput.focus();
      performSearch('');
    });

    // Keyboard Shortcuts (Ctrl+K, Cmd+K, Escape)
    document.addEventListener('keydown', e => {
      if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k') {
        e.preventDefault();
        if (searchModal.classList.contains('active')) {
          closeSearchModal();
        } else {
          openSearchModal();
        }
      } else if (e.key === 'Escape') {
        if (searchModal.classList.contains('active')) {
          closeSearchModal();
        }
        closeMobileSidebar();
      }
    });

    // Print Action
    printBtn.addEventListener('click', () => {
      window.print();
    });

    // Scroll to Top
    window.addEventListener('scroll', () => {
      if (window.scrollY > 400) {
        backToTopBtn.classList.add('visible');
      } else {
        backToTopBtn.classList.remove('visible');
      }
    });

    backToTopBtn.addEventListener('click', () => {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });

    // Hashchange listener for browser forward/backward
    window.addEventListener('hashchange', () => {
      handleInitialRoute();
    });
  }

  // Run on DOM Ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
