const API_URL = 'http://127.0.0.1:8000'; // Your backend URL
// Register
async function register() {
  const username = document.getElementById('reg-username').value;
  const password = document.getElementById('reg-password').value;

  const res = await fetch(`${API_URL}/auth/register?username=${username}&password=${password}`, {
    method: 'POST'
  });

  const data = await res.json().catch(() => null);

  if (res.ok) {
    document.getElementById('message').style.color = 'green';
    document.getElementById('message').innerText = 'Registered successfully! You can login now.';
  } else {
    document.getElementById('message').style.color = 'red';
    document.getElementById('message').innerText = data?.detail || 'Registration failed';
  }
}

// Login
async function login() {
  const username = document.getElementById('login-username').value;
  const password = document.getElementById('login-password').value;

  const res = await fetch(`${API_URL}/auth/login?username=${username}&password=${password}`, {
    method: 'POST'
  });

  const data = await res.json().catch(() => null);

  if (res.ok && data.access_token) {
    localStorage.setItem('token', data.access_token);
    window.location.href = 'dashboard.html';
  } else {
    document.getElementById('message').style.color = 'red';
    document.getElementById('message').innerText = data?.detail || 'Login failed';
  }
}

// Check token on dashboard load
window.onload = () => {
  if (window.location.pathname.includes('dashboard.html')) {
    const token = localStorage.getItem('token');
    if (!token) window.location.href = 'index.html';
  }
}

// Upload RAG
async function uploadRag() {
  const fileInput = document.getElementById('rag-file');
  const token = localStorage.getItem('token');

  if (!fileInput.files.length) {
    alert('Choose a file first');
    return;
  }

  const formData = new FormData();
  formData.append('file', fileInput.files[0]);

  const res = await fetch(`${API_URL}/rag/upload`, {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${token}`
    },
    body: formData
  });

  const data = await res.json().catch(() => null);

  document.getElementById('result').innerText = data?.detail || 'Uploaded!';
}

// Logout
function logout() {
  localStorage.removeItem('token');
  window.location.href = 'index.html';
}

// Example: upload file
async function uploadFile(file, token) {
  const formData = new FormData();
  formData.append("file", file);

  const res = await fetch(`${API_URL}/rag/upload`, {
    method: "POST",
    body: formData,
    headers: {
      "Authorization": `Bearer ${token}`
    }
  });
  return res.json();
}
