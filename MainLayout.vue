<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated class>
      <div class="row justify-between items-center">
        <!-- Logo -->
        <div>
          <img
            src="Hidden to make code public"
            alt="Logo"
            style="width: 115px"
          />
        </div>

        <!--LOS TABS-->>
        <div class="q-pa-md">
          <q-toolbar class="text-secondary" style="justify-content: center">
            <q-space />
            <q-tabs
              v-model="tab"
              shrink
              stretch
              allign="center"
              style="background-color: transparent"
            >
              <template>
                <div class="container">
                  <h4 class="text-center">
                    <strong
                      >Retailer, find products devaluation for <br
                    /></strong>
                    <span class="text-secondary">
                      <strong>product rentals & subscriptions</strong>
                    </span>
                  </h4>

                  <q-input
                    outlined
                    rounded
                    dense
                    color="secondary"
                    text-color="secondary"
                    label="Search a Product"
                    v-model="filtro"
                    class="search-input"
                  />

                  <q-btn
                    outline
                    no-caps
                    round
                    color="secondary"
                    class="custom-btn"
                    @click="onClick"
                  >
                    <img
                      src="Hidden to make code public"
                      alt="Logo Dog"
                      style="
                        width: 20px;
                        height: 20px;
                        position: fixed;
                        bottom: 10px;
                        right: 10px;
                      "
                    />
                  </q-btn>
                </div>
              </template>

              <q-route-tab
                to="/Products"
                unelevated
                rounded
                no-cap
                name="tab1"
                label="Product search"
              />
              <q-btn-dropdown
                unelevated
                rounded
                label="Products"
                class="rounded"
              >
                <q-list>
                  <q-item clickable @click="tab = 'Technology'">
                    <q-item-section>Technology</q-item-section>
                  </q-item>
                </q-list>
              </q-btn-dropdown>

              <q-route-tab
                to="/Compare"
                unelevated
                rounded
                name="tab2"
                label="Compare"
              />
              <q-route-tab
                to="/LastSearches"
                unelevated
                rounded
                name="tab3"
                label="Last Searches"
              />
              <q-route-tab
                to="/AboutUs"
                unelevated
                rounded
                name="tab4"
                label="About us"
              />
            </q-tabs>
          </q-toolbar>
        </div>
        <!-- Botones de Login y Sign Up -->
        <div>
          <q-btn
            color="white"
            outline
            text-color="#0B1AAD"
            label="Login"
            class="q-mr-md"
          />
          <q-btn
            outline
            no-caps
            rounded
            color="secondary"
            text-color="secondary"
            label="Login"
            class="q-mr-md"
          />
          <q-btn
            no-caps
            unelevated
            rounded
            color="secondary"
            text-color="#0B1AAD"
            label="Sign Up"
            class="q-mr-lg"
          />
        </div>
      </div>
    </q-header>
    <q-page-container>
      <keep-alive>
        <router-view />
      </keep-alive>
    </q-page-container>
  </q-layout>
</template>

<script>
import { defineComponent, ref } from "vue";
import EssentialLink from "components/EssentialLink.vue";

const linksList = [
  {
    title: "Docs",
    caption: "quasar.dev",
    icon: "school",
    link: "https://quasar.dev",
  },
  {
    title: "Github",
    caption: "github.com/quasarframework",
    icon: "code",
    link: "https://github.com/quasarframework",
  },
  {
    title: "Discord Chat Channel",
    caption: "chat.quasar.dev",
    icon: "chat",
    link: "https://chat.quasar.dev",
  },
  {
    title: "Forum",
    caption: "forum.quasar.dev",
    icon: "record_voice_over",
    link: "https://forum.quasar.dev",
  },
  {
    title: "Twitter",
    caption: "@quasarframework",
    icon: "rss_feed",
    link: "https://twitter.quasar.dev",
  },
  {
    title: "Facebook",
    caption: "@QuasarFramework",
    icon: "public",
    link: "https://facebook.quasar.dev",
  },
  {
    title: "Quasar Awesome",
    caption: "Community Quasar projects",
    icon: "favorite",
    link: "https://awesome.quasar.dev",
  },
];

export default defineComponent({
  name: "MainLayout",

  setup() {
    const tab = ref("tab1");
    const filtro = ref("");

    const onClick = () => {
      // Hidden to make code public
    };

    return {
      tab,
      filtro,
      onClick,
    };
  },
});

// Aquí se exporta el otro componente defineComponent
export const CalculadoraDepreciacion = defineComponent({
  name: "Hidden to make code public",
  data() {
    return {
      filtro: "",
    };
  },
  methods: {
    onClick() {
      // Hidden to make code public
    },
  },
});
</script>

<style scoped>
.container {
  position: relative;
}

.search-input {
  max-width: 300px; /* Ajusta el ancho máximo de la barra de búsqueda */
  margin: 0 auto; /* Centra la barra de búsqueda horizontalmente */
  background-color: white; /* Fondo blanco */
  border-color: var(--q-color-secondary); /* Contorno de color secondary */
}

.text-secondary {
  color: var(--q-color-secondary);
}

.custom-btn {
  position: absolute;
  bottom: 10px;
  right: 10px;
}
.custom-tabs {
  margin-top: 100px; /* Ajusta el espacio entre los tabs */
}
.q-tab {
  text-transform: lowercase;
  font-size: 32px; /* Ajusta el tamaño de la letra */
  border-radius: 20px; /* Hace los bordes de los tabs redondos */
}
.q-btn-dropdown {
  text-transform: lowercase;
}
</style>

<style lang="scss">
.q-header {
  background-color: white;
}

.row {
  display: flex;
  align-items: center;
}

.q-btn {
  border-radius: 20px;
}
</style>
<!--Estilo de los tabs-->
