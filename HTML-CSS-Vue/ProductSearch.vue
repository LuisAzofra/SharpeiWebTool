//Only some products shown to demonstrate functionality
  <div class="container">
    <h4 class="text-center" style="margin-bottom: 20px; margin-top: 70px">
      <strong>Retailer, find products devaluation for <br /></strong>
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
      style="margin-top: 10px"
      @keyup.enter="searchAndRedirect"
    />
  </div>
  <div style="position: relative">
    <p
      class="rounded-border"
      style="
        display: inline-block;
        margin: 10px;
        margin-left: 150px;
        margin-top: 50px;
        vertical-align: top;
      "
    >
      Re-commerce Solutions
    </p>

    <h4
      class="texto-inf"
      style="
        display: block;
        margin: 0 10px 10px 150px; /* Margen inferior agregado para separar del siguiente texto */
        padding-top: 5px;
      "
    >
      <strong>Sharpei: Your All-in-One <br />Circular Platform</strong>
    </h4>

    <div
      style="
        position: absolute;
        top: 10px; /* Ajusta la altura según sea necesario */
        right: 100px; /* 100px de la derecha de la pantalla */
      "
    >
      <p
        class="textFino-inf"
        style="
          margin: 0;
          margin-right: 150px;
          padding-top: 70px;
          vertical-align: top;
          font-size: 16px;
        "
      >
        Try-before-buy, rentals, subscriptions, and second-hand
        <br />
        options, catering to diverse business needs, all in one place.
      </p>
      <q-btn
        no-caps
        color="secondary"
        rounded
        label="Request a Demo"
        class="button-bold"
        style="
          border-radius: 7px;
          color: white;
          margin-top: 20px;
          font-size: 16px;
          font-family: 'DM Sans Placeholder', sans-serif;
        "
      />

      <!-- Botón blanco con recuadro en color secundary -->
      <router-link to="/AboutUs">
        <q-btn
          no-caps
          outline
          color="secondary"
          rounded
          square
          label="About Us"
          class="button-bold2"
          style="
            border-radius: 7px;
            margin-top: 20px;
            margin-left: 10px;
            font-size: 16px !important;
            font-family: 'DM Sans Placeholder', sans-serif;
          "
        />
      </router-link>
    </div>
    <img
      src="icons/(Hidden to make code public)"
      alt="LifeAsAService"
      style="
        width: 500px;
        height: 500px;
        margin-top: 30px;
        margin-left: 590px;

        border-radius: 15px;
      "
    />

    <div
      class="textBajo"
      style="margin-top: -505px; margin-left: 150px; width: 400px"
    >
      <p
        class="p4"
        style="margin-left: 20px; margin-top: 10px; font-size: 15px"
      >
        <strong> Try-before-buy </strong>
      </p>
      <p class="interior" style="margin-left: 10px; margin-top: -10px">
        Let customers sample products risk-free, ensuring
        <br />satisfaction before purchase. It's the confidence-booster <br />
        your shopping needs.
      </p>
    </div>
    <div
      class="textBajo"
      style="margin-top: -30px; margin-left: 150px; width: 400px"
    >
      <p
        class="p4"
        style="margin-left: 20px; margin-top: 10px; font-size: 15px"
      >
        <strong> Daily Rentals </strong>
      </p>
      <p class="interior" style="margin-left: 10px; margin-top: -10px">
        Let your customers explore without ownership!
        <br />Rentals offer the freedom to enjoy items temporarily, <br />
        making informed decisions hassle-free
      </p>
    </div>
    <div
      class="textBajo"
      style="margin-top: -30px; margin-left: 150px; width: 400px"
    >
      <p
        class="p4"
        style="margin-left: 20px; margin-top: 10px; font-size: 15px"
      >
        <strong> Subscriptions </strong>
      </p>
      <p class="interior" style="margin-left: 10px; margin-top: -10px">
        Let your customers simplify their lives! With subscriptions,
        <br />
        they can enjoy products or services regularly, no strings <br />
        attached.
      </p>
    </div>
    <div
      class="textBajo"
      style="margin-top: -30px; margin-left: 150px; width: 400px"
    >
      <p
        class="p4"
        style="margin-left: 20px; margin-top: 10px; font-size: 15px"
      >
        <strong> Second-hand </strong>
      </p>
      <p class="interior" style="margin-left: 10px; margin-top: -10px">
        Let your customers rediscover treasures! Embrace the
        <br />
        charm of pre-loved items, finding quality pieces that come <br />
        with their unique stories and a renewed purpose.
      </p>
    </div>
  </div>
  <q-btn
    outline
    no-caps
    round
    color="secondary"
    class="custom-btn"
    @click="onClick"
    style="position: fixed; bottom: 20px; right: 20px"
  >
    <img
      src="icons/(Hidden to make code public)"
      alt="Logo Dog"
      style="
        width: 20px;
        height: 20px;
        position: absolute;
        bottom: 10px;
        right: 10px;
      "
    />
  </q-btn>
</template>

<script>
import { defineComponent } from "vue";

export default defineComponent({
  name: "Calculadora-Depreciacion",
  data() {
    return {
      filtro: "",
    };
  },
  methods: {
    onClick() {
      // Hidden to make code public
    },

    searchAndRedirect() {
      if (
        this.filtro.trim() === "iphone 15 512gb" ||
        this.filtro.trim() === "iphone 15"
      ) {
        sessionStorage.setItem("productName", "iphone15 512gb");
        sessionStorage.setItem("totalAmount", 1399);
        this.$router.push({ path: "/LastSearches" });
      } else if (this.filtro.trim() === "iphone 15 256gb") {
        sessionStorage.setItem("productName", "iphone15 256gb");
        sessionStorage.setItem("totalAmount", 1199);
        this.$router.push({ path: "/LastSearches" });
      } else if (this.filtro.trim() === "iphone 15 pro max 512gb") {
        sessionStorage.setItem("productName", "iphone15promax512gb");
        sessionStorage.setItem("totalAmount", 1899);
        this.$router.push({ path: "/LastSearches" });
      } else if (
        this.filtro.trim() === "iphone 15 pro max 1tb" ||
        this.filtro.trim() === "iphone 15 pro max"
      ) {
        sessionStorage.setItem("productName", "iphone15promax1tb");
        sessionStorage.setItem("totalAmount", 1999);
        this.$router.push({ path: "/LastSearches" });
      } else if (
        this.filtro.trim() === "iphone 15 plus 512gb" ||
        this.filtro.trim() === "iphone 15 plus"
      ) {
        sessionStorage.setItem("productName", "iphone15plus512gb");
        sessionStorage.setItem("totalAmount", 1599);
        this.$router.push({ path: "/LastSearches" });
      } else if (this.filtro.trim() === "iphone 15 plus 256gb") {
        sessionStorage.setItem("productName", "iphone15plus256gb");
        sessionStorage.setItem("totalAmount", 1399);
        this.$router.push({ path: "/LastSearches" });
      } else if (this.filtro.trim() === "iphone 15 plus 128gb") {
        sessionStorage.setItem("productName", "iphone15plus128gb");
        sessionStorage.setItem("totalAmount", 1299);
        this.$router.push({ path: "/LastSearches" });
      } else if (
        this.filtro.trim() === "iphone 15 pro 512gb" ||
        this.filtro.trim() === "iphone 15 pro"
      ) {
        sessionStorage.setItem("productName", "iphone15pro512gb");
        sessionStorage.setItem("totalAmount", 1599);
        this.$router.push({ path: "/LastSearches" });
      } else if (this.filtro.trim() === "iphone 15 pro 256gb") {
        sessionStorage.setItem("productName", "iphone15pro256gb");
        sessionStorage.setItem("totalAmount", 1499);
        this.$router.push({ path: "/LastSearches" });
      } else if (this.filtro.trim() === "iphone 15 pro 128gb") {
        sessionStorage.setItem("productName", "iphone15pro128gb");
        sessionStorage.setItem("totalAmount", 1399);
        this.$router.push({ path: "/LastSearches" });
      } else if (this.filtro.trim() === "iphone 15 pro max 256gb") {
        sessionStorage.setItem("productName", "iphone15promax256gb");
        sessionStorage.setItem("totalAmount", 1699);
        this.$router.push({ path: "/LastSearches" });
        //Iphone 14 pro max
      } else if (this.filtro.trim() === "iphone 14 pro max 512gb") {
        sessionStorage.setItem("productName", "iphone14promax512gb");
        sessionStorage.setItem("totalAmount", 1050);
        this.$router.push({ path: "/LastSearches" });
      } else if (this.filtro.trim() === "iphone 14 pro max 256gb") {
        sessionStorage.setItem("productName", "iphone14promax256gb");
        sessionStorage.setItem("totalAmount", 1010);
        this.$router.push({ path: "/LastSearches" });
      } else if (this.filtro.trim() === "iphone 14 pro max 1tb") {
        sessionStorage.setItem("productName", "iphone14promax1tb");
        sessionStorage.setItem("totalAmount", 1100);
        this.$router.push({ path: "/LastSearches" });
        //Iphone 14 pro
      } else if (this.filtro.trim() === "iphone 14 pro 512gb") {
        sessionStorage.setItem("productName", "iphone14pro512gb");
        sessionStorage.setItem("totalAmount", 1000);
        this.$router.push({ path: "/LastSearches" });
      } else if (this.filtro.trim() === "iphone 14 pro 256gb") {
        sessionStorage.setItem("productName", "iphone14pro256gb");
        sessionStorage.setItem("totalAmount", 950);
        this.$router.push({ path: "/LastSearches" });
      } else if (this.filtro.trim() === "iphone 14 pro 128gb") {
        sessionStorage.setItem("productName", "iphone14pro128gb");
        sessionStorage.setItem("totalAmount", 900);
        this.$router.push({ path: "/LastSearches" });
      } else if (this.filtro.trim() === "iphone 14 pro 1tb") {
        sessionStorage.setItem("productName", "iphone14pro1tb");
        sessionStorage.setItem("totalAmount", 1050);
        this.$router.push({ path: "/LastSearches" });
      }
      //Iphone 14 plus
      else if (this.filtro.trim() === "iphone 14 plus 512gb") {
        sessionStorage.setItem("productName", "iphone14plus512gb");
        sessionStorage.setItem("totalAmount", 1100);
        this.$router.push({ path: "/LastSearches" });
      } else if (this.filtro.trim() === "iphone 14 plus 256gb") {
        sessionStorage.setItem("productName", "iphone14plus256gb");
        sessionStorage.setItem("totalAmount", 1050);
        this.$router.push({ path: "/LastSearches" });
      } else if (this.filtro.trim() === "iphone 14 plus 128gb") {
        sessionStorage.setItem("productName", "iphone14plus128gb");
        sessionStorage.setItem("totalAmount", 1000);
        this.$router.push({ path: "/LastSearches" });
      }
      //Iphone 14
      else if (this.filtro.trim() === "iphone 14 512gb") {
        sessionStorage.setItem("productName", "iphone14 512gb");
        sessionStorage.setItem("totalAmount", 900);
        this.$router.push({ path: "/LastSearches" });
      } else if (this.filtro.trim() === "iphone 14 256gb") {
        sessionStorage.setItem("productName", "iphone14 256gb");
        sessionStorage.setItem("totalAmount", 850);
        this.$router.push({ path: "/LastSearches" });
      } else if (this.filtro.trim() === "iphone 14 128gb") {
        sessionStorage.setItem("productName", "iphone14 128gb");
        sessionStorage.setItem("totalAmount", 800);
        this.$router.push({ path: "/LastSearches" });
      }
    },
  },
});
</script>

<style scoped>
.textBajo {
  border: 1px solid #0b1aad;
  border-radius: 20px;
  background-color: rgb(255, 255, 255);
  box-shadow: 0px 10px 20px rgba(48, 63, 119, 0.06),
    0px 2px 6px rgba(48, 66, 120, 0.06), 0px 0px 1px rgba(48, 66, 120, 0.06);
  padding: 6px;
  width: fit-content; /* Para que el ancho se ajuste automáticamente al contenido */
  margin-left: 150px;
  margin-top: -90px;
  margin: 50px;
}
.interior {
  color: rgba(75, 81, 98, 0.806);
}
.button-bold {
  font-weight: bold !important;
}
.button-bold2 {
  font-weight: bold !important;
}
.rounded-border {
  margin-left: 150px;
  border: 1px solid rgb(209, 213, 226);
  border-radius: 20px;
  background-color: #ffffff;
  box-shadow: 0px 10px 20px rgba(48, 63, 119, 0.06),
    0px 2px 6px rgba(48, 66, 120, 0.06), 0px 0px 1px rgba(48, 66, 120, 0.06);
  padding: 6px;
  width: fit-content; /* Para que el ancho se ajuste automáticamente al contenido */
  margin-top: 150px;
  margin: 0; /* Para quitar el margen predeterminado del párrafo */
  font-family: "Inter", sans-serif; /* Cambiar la fuente si es necesario */
  font-weight: 500; /* Cambiar el peso de la fuente si es necesario */
  text-align: center; /* Centrar el texto */
  color: rgb(75, 81, 98); /* Cambiar el color del texto si es necesario */
  letter-spacing: 1px;
}

.container {
  position: relative;
}
.texto-inf {
  margin-left: 100px;
}
.textFino-inf {
  margin-right: 100px;
  color: rgba(75, 81, 98, 0.806);
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
  bottom: 0px;
  right: 10px;
}
</style>
./ProductSearch.vue
