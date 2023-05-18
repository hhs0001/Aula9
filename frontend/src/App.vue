<template>
  <div id="app">
    <header>
      <h1>BookList</h1>
    </header>
    <main>
      <book-list />
    </main>
  </div>
</template>

<script>
import BookList from "./components/BookList.vue";

export default {
  components: {
    BookList,
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
