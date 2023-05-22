import { createRouter, createWebHistory } from 'vue-router'
import LandingPage from "@/components/LandingPage.vue";
import reactionTest from "@/components/ReactionTest.vue";
import FirstBeer from "@/components/FirstBeer.vue";
import ConsecutiveBeers from "@/components/ConsecutiveBeers.vue";
import CupCollection from "@/components/CupCollection.vue";
import Leaderboard from "@/components/Leaderboard.vue";
import Payment from "@/components/Payment.vue";
import Checkout from "@/components/Checkout.vue";
import PaymentSuccessful from "@/components/PaymentSuccessful.vue";

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
    {
    path: "/checkout/:product/:id/:discount",
    name: "checkout",
    component: Checkout
    },
    {
    path: "/payment/:id/:type/:product/:price",
    name: "payment",
    component: Payment
    },
    {
    path: "/payment_success/:id",
    name: "paymentsuccess",
    component: PaymentSuccessful
    },
    {
    path: "/leaderboard/:id",
    name: "leaderboard",
    component: Leaderboard
    },
  ]
})

export default router
