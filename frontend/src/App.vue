<script setup lang="ts">
</script>

<template>
  <div id="app">
    <header>
      <h1>TaskZen</h1>
    </header>
    <main>
      <login-form v-if="!loggedIn && !showRegister" @login-success="loginSuccess" @go-to-register="showRegister = true" />
      <register-form v-if="!loggedIn && showRegister" @register-success="loginSuccess" @go-to-login="showRegister = false" />
      <task-list v-if="loggedIn" />
    </main>
  </div>
</template>

<script>
import LoginForm from "./components/LoginForm.vue";
import RegisterForm from "./components/RegisterForm.vue";
import TaskList from "./components/TaskList.vue";

export default {
  components: {
    LoginForm,
    RegisterForm,
    TaskList,
  },
  data() {
    return {
      loggedIn: false,
      showRegister: false,
    };
  },
  methods: {
    loginSuccess() {
      this.loggedIn = true;
      this.$refs.taskList.loadTasks();
    },
  },
};
</script>

<style>
* {
  box-sizing: border-box;
}

body {
  margin: 0;
  font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
  background-color: #f0f0f0;
}

header {
  background-color: #4caf50;
  padding: 1rem 2rem;
  color: white;
}

main {
  padding: 2rem;
}
</style>
