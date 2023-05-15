import { createRouter, createWebHistory } from 'vue-router'
import Books from '../components/Books.vue'
import Ping from '../components/Ping.vue'
import LandingPage from "@/components/LandingPage.vue";
import LoginPage from "@/components/LoginPage.vue";
import Video from "@/components/Video.vue";
import reactionTest from "@/components/ReactionTest.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/book',
      name: 'Books',
      component: Books,
    },
    {
      path: '/ping',
      name: 'ping',
      component: Ping
    },
    {
      path: '/',
      name: 'landing',
      component: LandingPage
    },
    {
      path: '/login',
      name: 'login',
      component: LoginPage
    },
    {
      path: '/video',
      name: 'video',
      component: Video
    },
    {
      path: '/reactiontest',
      name: 'reactiontest',
      component: reactionTest
    }
  ]
})

export default router
