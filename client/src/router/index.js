import { createRouter, createWebHistory } from 'vue-router'
import Books from '../components/Books.vue'
import LandingPage from "@/components/LandingPage.vue";
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
      path: '/',
      name: 'landing',
      component: LandingPage
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
