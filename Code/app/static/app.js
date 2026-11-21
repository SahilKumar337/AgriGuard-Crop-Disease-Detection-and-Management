// AgriGuard ChatGPT-Style Multimodal Frontend Logic
// Course: CSE471 | AIML Engineering Pipeline

// Register Service Worker for offline Android execution
if ('serviceWorker' in navigator) {
  window.addEventListener('load', () => {
    navigator.serviceWorker.register('/sw.js')
      .then(reg => console.log('[AgriGuard SW] Registered with scope:', reg.scope))
      .catch(err => console.error('[AgriGuard SW] Registration failed:', err));
  });
}

// State
let attachedFile = null;
let currentConversation = [];

// DOM Elements
const chatMessages = document.getElementById('chat-messages');
const chatInput = document.getElementById('chat-input');
const attachmentPreview = document.getElementById('attachment-preview');
const attachmentThumb = document.getElementById('attachment-thumb');
const attachmentName = document.getElementById('attachment-name');
const sliderTemp = document.getElementById('slider-temp');
const sliderHum = document.getElementById('slider-hum');
const lblTemp = document.getElementById('lbl-temp');
const lblHum = document.getElementById('lbl-hum');
const sidebar = document.getElementById('sidebar');

function toggleSidebar() {
  sidebar.classList.toggle('open');
}

function updateSensorLabels() {
  lblTemp.innerText = `${parseFloat(sliderTemp.value).toFixed(1)} °C`;
  lblHum.innerText = `${parseFloat(sliderHum.value).toFixed(1)} %`;
}

function handleFileSelected(event) {
  if (event.target.files && event.target.files[0]) {
    attachedFile = event.target.files[0];
    showAttachmentPreview(attachedFile);
  }
}

function showAttachmentPreview(file) {
  attachmentName.innerText = file.name;
  const reader = new FileReader();
  reader.onload = (e) => {
    attachmentThumb.src = e.target.result;
    attachmentPreview.style.display = 'flex';
    chatInput.focus();
  };
  reader.readAsDataURL(file);
}

function clearAttachment() {
  attachedFile = null;
  attachmentPreview.style.display = 'none';
  document.getElementById('camera-file').value = '';
  document.getElementById('gallery-file').value = '';
}

function handleKeyDown(event) {
  if (event.key === 'Enter' && !event.shiftKey) {
    event.preventDefault();
    sendMessage();
  }
}

// Send Message Flow
async function sendMessage(overrideText = null, overrideFile = null) {
  const text = (overrideText !== null) ? overrideText : chatInput.value.trim();
  const file = (overrideFile !== null) ? overrideFile : attachedFile;

  if (!text && !file) {
    return;
  }

  // Append user message
  appendUserMessage(text, file);

  // Clear inputs
  if (overrideText === null) chatInput.value = '';
  if (overrideFile === null) clearAttachment();

  // Append typing indicator
  const typingId = appendTypingIndicator();

  // Prepare payload
  const formData = new FormData();
  formData.append('message', text);
  if (file) {
    formData.append('file', file);
  }
  formData.append('temperature', parseFloat(sliderTemp.value));
  formData.append('humidity', parseFloat(sliderHum.value));

  try {
    const response = await fetch('/api/chat', {
      method: 'POST',
      body: formData
    });

    if (!response.ok) {
      throw new Error(`Server returned HTTP ${response.status}`);
    }

    const json = await response.json();
    removeTypingIndicator(typingId);
    appendAssistantMessage(json.data);
  } catch (err) {
    console.error('Chat error:', err);
    removeTypingIndicator(typingId);
    appendAssistantFallback(text, file);
  }
}

function appendUserMessage(text, file) {
  const row = document.createElement('div');
  row.className = 'message-row user';

  let fileHtml = '';
  if (file) {
    const url = URL.createObjectURL(file);
    fileHtml = `<img src="${url}" class="user-leaf-thumb" alt="Uploaded leaf">`;
  }

  row.innerHTML = `
    <div class="avatar user">👤</div>
    <div class="bubble">
      ${fileHtml}
      ${text ? `<p>${escapeHtml(text)}</p>` : ''}
    </div>
  `;
  chatMessages.appendChild(row);
  scrollToBottom();
}

function appendTypingIndicator() {
  const id = 'typing-' + Date.now();
  const row = document.createElement('div');
  row.className = 'message-row ai';
  row.id = id;
  row.innerHTML = `
    <div class="avatar ai">🌱</div>
    <div class="bubble">
      <div class="typing-dots">
        <div class="typing-dot"></div>
        <div class="typing-dot"></div>
        <div class="typing-dot"></div>
      </div>
    </div>
  `;
  chatMessages.appendChild(row);
  scrollToBottom();
  return id;
}

function removeTypingIndicator(id) {
  const el = document.getElementById(id);
  if (el) el.remove();
}

function appendAssistantMessage(data) {
  const row = document.createElement('div');
  row.className = 'message-row ai';

  let yoloHtml = '';
  if (data.annotated_image_b64) {
    const meta = data.detection_meta;
    yoloHtml = `
      <div class="yolo-annotated-card">
        <div class="yolo-tag">
          <span>🎯 YOLO Lesions Localized: ${meta.lesion_count}</span>
          <span>Severity: ${meta.severity_pct}% (${meta.severity_stage})</span>
        </div>
        <img src="${data.annotated_image_b64}" alt="YOLO Annotated Bounding Boxes">
      </div>
    `;
  }

  const parsedMarkdown = renderSimpleMarkdown(data.response_text);

  row.innerHTML = `
    <div class="avatar ai">🌱</div>
    <div class="bubble">
      ${yoloHtml}
      ${parsedMarkdown}
    </div>
  `;
  chatMessages.appendChild(row);
  scrollToBottom();
}

function appendAssistantFallback(text, file) {
  const fallbackData = {
    response_text: `### ⚠️ Network Disruption - Local Agronomic Guidance
I noticed a temporary interruption communicating with the neural server.

**Standard Field Recommendations:**
- If examining **Tomato foliage** with concentric dark rings, this indicates **Early Blight** (*Alternaria solani*).
- **Bio-Control:** Apply *Trichoderma viride* (2.5 kg/ha) or Neem oil 1500 ppm at 3 ml/L.
- **Chemical Control:** Preventive spray of Chlorothalonil 75% WP (3 g/L water) with 7-day Pre-Harvest Interval (PHI).
- Maintain drip irrigation and avoid overhead wetting.`,
    annotated_image_b64: null,
    detection_meta: null
  };
  appendAssistantMessage(fallbackData);
}

// Quick Sample Loaders
function loadSamplePrompt(sampleType) {
  const sampleMap = {
    'tomato_early': {
      path: '/Data/sample_images/tomato_early_blight_sample.jpg',
      query: 'Please analyze this tomato leaf for early signs of blight.'
    },
    'potato_late': {
      path: '/Data/sample_images/potato_late_blight_sample.jpg',
      query: 'Are these lesions on my potato foliage late blight? What chemical should I spray?'
    },
    'apple_scab': {
      path: '/Data/sample_images/apple_scab_sample.jpg',
      query: 'Inspect my apple leaf scabs and provide IPM treatment recommendations.'
    },
    'pest_damage': {
      path: '/Data/sample_images/pest_infestation_sample.jpg',
      query: 'Identify the pest damage on my maize leaf and give biological controls.'
    },
    'healthy_leaf': {
      path: '/Data/sample_images/tomato_healthy_sample.jpg',
      query: 'Check if this crop foliage is completely healthy.'
    }
  };

  const item = sampleMap[sampleType] || sampleMap['tomato_early'];

  fetch(item.path)
    .then(res => res.blob())
    .then(blob => {
      const file = new File([blob], `${sampleType}.jpg`, { type: 'image/jpeg' });
      sendMessage(item.query, file);
      if (window.innerWidth <= 768) toggleSidebar();
    })
    .catch(err => {
      console.log('Sample fetch local fallback');
      sendMessage(item.query, null);
    });
}

function handleChipClick(sampleType) {
  loadSamplePrompt(sampleType);
}

function sendQuickText(text) {
  sendMessage(text, null);
}

function startNewChat() {
  chatMessages.innerHTML = '';
  // Reload greeting
  location.reload();
}

function loadHistoryItem(type) {
  if (type === 'knapsack') {
    sendQuickText('How do I calculate chemical dosage for a 15-liter backpack sprayer?');
  } else if (type === 'organic') {
    sendQuickText('What are the best organic and bio-pesticides for fungal leaf spots?');
  } else if (type === 'weather') {
    sendQuickText('How do temperature and humidity affect fungal spore germination and spray timing?');
  }
  if (window.innerWidth <= 768) toggleSidebar();
}

function scrollToBottom() {
  setTimeout(() => {
    chatMessages.scrollTop = chatMessages.scrollHeight;
  }, 50);
}

function escapeHtml(str) {
  return str.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
}

function renderSimpleMarkdown(md) {
  if (!md) return '';
  let html = md
    .replace(/^### (.*$)/gim, '<h3>$1</h3>')
    .replace(/^#### (.*$)/gim, '<h4>$1</h4>')
    .replace(/^\> (.*$)/gim, '<blockquote>$1</blockquote>')
    .replace(/\*\*(.*?)\*\*/gim, '<strong>$1</strong>')
    .replace(/\*(.*?)\*/gim, '<em>$1</em>')
    .replace(/`([^`]+)`/gim, '<code>$1</code>')
    .replace(/^---$/gim, '<hr>')
    .replace(/\n\n/gim, '<br><br>');
  return html;
}
