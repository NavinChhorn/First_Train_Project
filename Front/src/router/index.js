import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import TaskView from '../views/TaskView.vue'
import TaskDetailView from '../views/TaskDetailView.vue'
import ErrorPage from '../../ErrorView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/task',
      name: 'task',
      component: TaskView
    },
    {
      path: '/detail/:index',
      name: 'detail',
      component: TaskDetailView
    },
    {
      path: '/:catchAll(.*)',
      component: ErrorPage
    },
  ]
})

export default router
