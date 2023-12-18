<template>
  <header class="bg-secondary p-3">
    <div class="wrapper">
      <nav class='d-flex'>
        <RouterLink to="/" class="text-white  m-2">Home</RouterLink>
        <RouterLink to="/task" class="text-white  m-2">Task</RouterLink>
      </nav>
    </div>
  </header>
  <RouterView />

  <div class='d-flex bg-secondary mt-auto'>
      <footer class="p-3">
        <div class="wrapper">
          <div class="text-center">
            <p class="m-0 text-white">Copyright &copy; 2020</p>
          </div>
        </div>
      </footer>
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<style>
#app {
  display: flex;
  flex-direction: column;
  width: 100%;
  max-width: 100%;
  min-height: 100vh;
}

</style>