<template>
  <div>
    <h2>Lista de Tarefas</h2>
    <form @submit.prevent="addTask">
      <input type="text" v-model="newTask" placeholder="Digite uma nova tarefa" required />
      <button type="submit">Adicionar</button>
    </form>
    <ul>
      <li v-for="task in tasks" :key="task._id">
        {{ task.description }}
        <button @click="deleteTask(task._id)">Excluir</button>
        <button @click="showUpdateTaskForm(task)">Atualizar</button>
      </li>
    </ul>
    <div v-if="taskBeingEdited">
      <h3>Editar Tarefa</h3>
      <form @submit.prevent="updateTaskAndHideForm">
        <input type="text" v-model="taskBeingEdited.description" required />
        <button type="submit">Salvar</button>
        <button type="button" @click="taskBeingEdited = null">Cancelar</button>
      </form>
    </div>
  </div>
</template>


<script>
import { getTasks, createTask, updateTask, deleteTask } from "../api";

export default {
  data() {
    return {
      tasks: [],
      newTask: "",
      taskBeingEdited: null,
    };
  },
  methods: {
    async loadTasks() {
      this.tasks = await getTasks();
    },
    async addTask() {
      const task = {
        description: this.newTask,
        done: false,
      };
      const createdTask = await createTask(task);
      this.tasks.push(createdTask);
      this.newTask = "";
    },
    async deleteTask(taskId) {
      await deleteTask(taskId);
      this.tasks = this.tasks.filter((task) => task._id !== taskId);
    },
    showUpdateTaskForm(task) {
      this.taskBeingEdited = task;
  },
    async updateTaskAndHideForm() {
      await updateTask(this.taskBeingEdited._id, this.taskBeingEdited);
      this.taskBeingEdited = null;
  },
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
  