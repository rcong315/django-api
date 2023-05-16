import { createWebHistory, createRouter } from "vue-router";

const routes =  [
  {
    path: "/",
    alias: "/cars",
    name: "cars",
    component: () => import("./components/CarsList")
  },
  {
    path: "/cars/:pk",
    name: "car-details",
    component: () => import("./components/Car")
  },
  {
    path: "/add",
    name: "add",
    component: () => import("./components/AddCar")
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;