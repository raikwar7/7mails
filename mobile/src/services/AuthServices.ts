// src/services/api.ts

const BASE_URL = "http://localhost:8000";

export async function login(email: string, password: string) {
  const res = await fetch(`${BASE_URL}/login`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ email, password }),
  });

  return res.json();
}

export async function fetchMails(token: string) {
  const res = await fetch(`${BASE_URL}/mail`, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });

  return res.json();
}

export async function sendMail(data: any, token: string) {
  const res = await fetch(`${BASE_URL}/send-mail`, {
    method: "POST",

    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${token}`,
    },

    body: JSON.stringify(data),
  });

  return res.json();
}