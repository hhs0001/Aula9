<!-- src/components/LoginForm.vue -->
<template>
    <div>
      <h2>Login</h2>
      <form @submit.prevent="login">
        <input type="text" v-model="username" placeholder="Username" required />
        <input type="password" v-model="password" placeholder="Password" required />
        <button type="submit">Login</button>
      </form>
      <button @click="$emit('go-to-register')">Registrar</button>
    </div>
  </template>
  
  <script>
  import { loginUser } from "../api";
  
  export default {
    data() {
      return {
        username: "",
        password: "",
      };
    },
    methods: {
      async login() {
        try {
          const user = {
            username: this.username,
            password: this.password,
          };
          await loginUser(user);
          this.$emit('login-success');
        } catch (error) {
          console.error(error);
          alert('Login falhou');
        }
      },
    },
  };
  </script>
  
  <style scoped>
  form {
    display: flex;
    flex-direction: column;
    width: 300px;
    margin: 0 auto;
  }
  
  input, button {
    margin-bottom: 1rem;
  }
  </style>
  