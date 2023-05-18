<template>
  <div>
    <h2>Lista de Livros</h2>
    <form @submit.prevent="addBook">
      <input type="text" v-model="newBook.title" placeholder="Digite o título do livro" required />
      <input type="text" v-model="newBook.authors" placeholder="Digite os autores do livro" required />
      <input type="text" v-model="newBook.publisher" placeholder="Digite a editora do livro" required />
      <input type="number" v-model="newBook.year" placeholder="Digite o ano do livro" required />
      <input type="text" v-model="newBook.isbn" placeholder="Digite o ISBN do livro" required />
      <input type="number" v-model="newBook.price" placeholder="Digite o preço do livro" required />
      <button type="submit">Adicionar</button>
    </form>
    <ul>
      <li v-for="book in books" :key="book._id">
        <div>
          <strong>Título:</strong> {{ book.title }}
        </div>
        <div>
          <strong>Autores:</strong> {{ book.authors }}
        </div>
        <div>
          <strong>Editora:</strong> {{ book.publisher }}
        </div>
        <div>
          <strong>Ano:</strong> {{ book.year }}
        </div>
        <div>
          <strong>ISBN:</strong> {{ book.isbn }}
        </div>
        <div>
          <strong>Preço:</strong> {{ book.price }}
        </div>
        <button @click="deleteBook(book._id)">Excluir</button>
        <button @click="showUpdateBookForm(book)">Atualizar</button>
      </li>
    </ul>
    <div v-if="bookBeingEdited">
      <h3>Editar Livro</h3>
      <form @submit.prevent="updateBookAndHideForm">
        <input type="text" v-model="bookBeingEdited.title" required />
        <input type="text" v-model="bookBeingEdited.authors" required />
        <input type="text" v-model="bookBeingEdited.publisher" required />
        <input type="number" v-model="bookBeingEdited.year" required />
        <input type="text" v-model="bookBeingEdited.isbn" required />
        <input type="number" v-model="bookBeingEdited.price" required />
        <button type="submit">Salvar</button>
        <button type="button" @click="bookBeingEdited = null">Cancelar</button>
      </form>
    </div>
  </div>
</template>


<script>
import { getBooks, createBook, updateBook, deleteBook } from "../api";

export default {
  data() {
    return {
      books: [],
      newBook: {
        title: "",
        authors: "",
        publisher: "",
        year: "",
        isbn: "",
        price: "",
      },
      bookBeingEdited: null,
    };
  },
  methods: {
    async loadBooks() {
      this.books = await getBooks();
    },
    async addBook() {
      const createdBook = await createBook(this.newBook);
      this.books.push(createdBook);
      this.newBook = { title: "", authors: "", publisher: "", year: "", isbn: "", price: "" };
    },
    async deleteBook(bookId) {
      await deleteBook(bookId);
      this.books = this.books.filter((book) => book._id !== bookId);
    },
    showUpdateBookForm(book) {
      this.bookBeingEdited = book;
    },
    async updateBookAndHideForm() {
      await updateBook(this.bookBeingEdited._id, this.bookBeingEdited);
      this.bookBeingEdited = null;
    },
  },
  mounted() {
    this.loadBooks();
  },
};
</script>

<!-- Add your scoped styles here -->

  
  <style scoped>
  form {
    display: flex;
    margin-bottom: 1rem;
  }
  
  input {
    flex-grow: 1;
    padding: 0.5rem;
    margin-right: 0.5rem;
  }
  
  button {
    padding: 0.5rem;
    background-color: #4caf50;
    color: white;
    border: none;
    cursor: pointer;
  }
  
  button:hover {
    background-color: #3d8b40;
  }
  
  li {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: white;
    padding: 0.5rem;
    margin-bottom: 0.5rem;
  }
  
  li:nth-child(odd) {
    background-color: #f9f9f9;
  }
  </style>
  