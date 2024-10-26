const routes = [
  {
    path: "/",
    redirect: "/Products",
    component: () => import("layouts/MainLayout.vue"),
    children: [
      {
        path: "Products",
        component: () => import("pages/Products.vue"),
      },
      {
        path: "productSearch",
        component: () => import("pages/productSearch.vue"),
      },
      {
        path: "Compare",
        component: () => import("src/pages/Compare.vue"),
      },
      {
        path: "LastSearches",
        component: () => import("pages/LastSearches.vue"),
      },
      {
        path: "AboutUs",
        component: () => import("pages/AboutUs.vue"),
      },
    ],
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: "/:catchAll(.*)*",
    component: () => import("pages/ErrorNotFound.vue"),
  },
];

export default routes;
