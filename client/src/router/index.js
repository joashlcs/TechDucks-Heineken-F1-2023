import { createRouter, createWebHistory } from 'vue-router'
import Books from '../components/Books.vue'
import LandingPage from "@/components/LandingPage.vue";
import Video from "@/components/Video.vue";
import reactionTest from "@/components/ReactionTest.vue";
import FirstBeer from "@/components/FirstBeer.vue";
import ConsecutiveBeers from "@/components/ConsecutiveBeers.vue";
import CupCollection from "@/components/CupCollection.vue";

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
      path: '/returnuser/:id',
      name: 'returnUser',
      component: CupCollection
    },
    {
      path: '/reactiontest/:id/:status',
      name: 'reactiontest',
      component: reactionTest
    },
    {
      path: '/firstbeer/:id/:result',
      name: 'firstbeer',
      component: FirstBeer
    },
    {
    path: "/consecutivebeer/:id/:result",
    name: "consecutivebeer",
    component: ConsecutiveBeers
  },
  ]
})

export default router
