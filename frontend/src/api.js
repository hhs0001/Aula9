// src/api.js
const API_URL = "http://localhost:5000/books";

async function fetchData(url, options) {
  const response = await fetch(url, options);
  if (!response.ok) {
    throw new Error(`Failed to fetch: ${response.status}`);
  }
  return response.json();
}

export async function getBooks() {
  return fetchData(`${API_URL}/books`);
}

export async function createBook(book) {
  return fetchData(`${API_URL}/books`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(book),
  });
}

export async function updateBook(bookId, book) {
  return fetchData(`${API_URL}/books/${bookId}`, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(book),
  });
}

export async function deleteBook(bookId) {
  return fetchData(`${API_URL}/books/${bookId}`, {
    method: "DELETE",
  });
}

export async function loginUser(user) {
  return fetchData(`${API_URL}/login`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(user),
  });
}

export async function registerUser(user) {
  return fetchData(`${API_URL}/users`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(user),
  });
}
