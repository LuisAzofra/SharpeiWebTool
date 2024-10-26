//Only some products shown to make code public
<template>
  <div>
    <h4
      style="
        margin-bottom: 5px;
        margin-left: 310px;
        margin-top: 120px;
        color: #0b1aad;
      "
    >
      <strong>Use Sharpei.</strong>
    </h4>
    <p
      style="
        margin-top: 0;
        margin-bottom: 5px;
        margin-bottom: 5px;
        margin-left: 350px;
        font-size: 16px;
        color: black;
      "
    >
      <strong> You could earn</strong>
    </p>
    <p
      style="
        margin-top: 0;
        margin-bottom: 5px;
        margin-left: 330px;
        font-size: 46px;
        color: black;
      "
    >
      <strong
        >$
        {{
          Number.isInteger((totalAmount / 24) * sliderValue)
            ? (totalAmount / 24) * sliderValue
            : ((totalAmount / 24) * sliderValue).toFixed(0)
        }}</strong
      >
    </p>
    <p
      style="
        margin-top: 0;
        margin-bottom: 5px;
        margin-left: 250px;
        font-size: 16px;
        color: black;
      "
    >
      <u>{{ sliderValue }} Months</u> at an estimated $
      {{ (totalAmount / 24).toFixed(2) }} a Month
    </p>
  </div>
  <div class="q-pa-md">
    <q-slider
      v-model="sliderValue"
      :min="1"
      :max="24"
      label
      color="secondary"
      class="custom-slider"
    />
    <p
      style="
        margin-top: 0;
        margin-bottom: 5px;
        margin-left: 285px;
        font-size: 13px;
        color: rgb(75, 81, 98);
      "
    >
      <u>Learn how we estimate your earnings</u>
    </p>
    <p
      style="
        margin-top: 0;
        margin-bottom: 5px;
        margin-left: 285px;
        font-size: 13px;
        color: rgb(11, 26, 173);
      "
    >
      <u
        ><strong>Now searching: {{ productName }}</strong></u
      >
    </p>
    <div style="float: right; margin-top: -320px">
      <img
        :src="getImageUrl()"
        :alt="productName"
        style="width: 400px; margin-right: 200px; height: 400px"
      />
    </div>
  </div>
  <div
    class="seleccionar"
    v-if="
      productName === 'iphone15' ||
      productName === 'iphone15 128gb' ||
      productName === 'iphone15 256gb' ||
      productName === 'iphone15 512gb'
    "
  >
    <p
      style="
        color: rgba(75, 81, 98, 0.806);
        margin-left: 30px;
        margin-bottom: 0px;
        margin-top: -15px;
      "
    >
      Product Variants:
    </p>
    <select
      rounded
      outlined
      v-model="selectedVariant"
      @change="updateProductName"
      style="
        border: 1px solid #0b1aad;
        border-radius: 10px;
        color: rgba(75, 81, 98, 0.806);

        margin-left: 20px;
      "
    >
      <label class="placeholder">Product Variants</label>
      <option value="iphone15 128gb">iPhone 15 128GB</option>
      <option value="iphone15 256gb">iPhone 15 256GB</option>
      <option value="iphone15 512gb">iPhone 15 512GB</option>
    </select>
  </div>
  >
  <div
    class="seleccionar"
    v-if="
      productName === 'iphone15promax' ||
      productName === 'iphone15promax256gb' ||
      productName === 'iphone15promax512gb' ||
      productName === 'iphone15promax1tb'
    "
  >
    <p
      style="
        color: rgba(75, 81, 98, 0.806);
        margin-left: 40px;
        margin-bottom: 0px;
        margin-top: -30px;
      "
    >
      Product Variants:
    </p>
    <select
      rounded
      outlined
      v-model="selectedVariant"
      @change="updateProductName"
      style="
        border: 1px solid #0b1aad;
        border-radius: 10px;
        color: rgba(75, 81, 98, 0.806);
      "
    >
      <label class="placeholder">Product Variants</label>
      <option value="iphone15promax256gb">iPhone 15 Pro Max 256GB</option>
      <option value="iphone15promax512gb">iPhone 15 Pro Max 512GB</option>
      <option value="iphone15promax1tb">iPhone 15 Pro Max 1TB</option>
    </select>
  </div>
  <div
    class="seleccionar"
    v-if="
      productName === 'iphone15pro' ||
      productName === 'iphone15pro256gb' ||
      productName === 'iphone15pro512gb' ||
      productName === 'iphone15pro128gb'
    "
  >
    <p
      style="
        color: rgba(75, 81, 98, 0.806);
        margin-left: 30px;
        margin-bottom: 0px;
        margin-top: -30px;
      "
    >
      Product Variants:
    </p>
    <select
      rounded
      outlined
      v-model="selectedVariant"
      @change="updateProductName"
      style="
        border: 1px solid #0b1aad;
        border-radius: 10px;
        color: rgba(75, 81, 98, 0.806);
      "
    >
      <label class="placeholder">Product Variants</label>
      <option value="iphone15pro128gb">iPhone 15 Pro 128GB</option>
      <option value="iphone15pro256gb">iPhone 15 Pro 256GB</option>
      <option value="iphone15pro512gb">iPhone 15 Pro 512GB</option>
    </select>
  </div>
  <div
    class="seleccionar"
    v-if="
      productName === 'iphone15plus' ||
      productName === 'iphone15plus256gb' ||
      productName === 'iphone15plus512gb' ||
      productName === 'iphone15plus128gb'
    "
  >
    <p
      style="
        color: rgba(75, 81, 98, 0.806);
        margin-left: 30px;
        margin-bottom: 0px;
        margin-top: -30px;
      "
    >
      Product Variants:
    </p>
    <select
      rounded
      outlined
      v-model="selectedVariant"
      @change="updateProductName"
      style="
        border: 1px solid #0b1aad;
        border-radius: 10px;
        color: rgba(75, 81, 98, 0.806);
      "
    >
      <label class="placeholder">Product Variants</label>
      <option value="iphone15plus128gb">iPhone 15 Plus 128GB</option>
      <option value="iphone15plus256gb">iPhone 15 Plus 256GB</option>
      <option value="iphone15plus512gb">iPhone 15 Plus 512GB</option>
    </select>
  </div>
  <div
    class="seleccionar"
    v-if="
      productName === 'iphone14' ||
      productName === 'iphone14 128gb' ||
      productName === 'iphone14 256gb' ||
      productName === 'iphone14 512gb'
    "
  >
    <p
      style="
        color: rgba(75, 81, 98, 0.806);
        margin-left: 30px;
        margin-bottom: 0px;
        margin-top: -15px;
      "
    >
      Product Variants:
    </p>
    <select
      rounded
      outlined
      v-model="selectedVariant"
      @change="updateProductName"
      style="
        border: 1px solid #0b1aad;
        border-radius: 10px;
        color: rgba(75, 81, 98, 0.806);

        margin-left: 20px;
      "
    >
      <label class="placeholder">Product Variants</label>
      <option value="iphone14 128gb">iPhone 14 128GB</option>
      <option value="iphone14 256gb">iPhone 14 256GB</option>
      <option value="iphone14 512gb">iPhone 14 512GB</option>
    </select>
  </div>
  >
  <div
    class="seleccionar"
    v-if="
      productName === 'iphone14promax' ||
      productName === 'iphone14promax256gb' ||
      productName === 'iphone14promax512gb' ||
      productName === 'iphone14promax1tb'
    "
  >
    <p
      style="
        color: rgba(75, 81, 98, 0.806);
        margin-left: 40px;
        margin-bottom: 0px;
        margin-top: -30px;
      "
    >
      Product Variants:
    </p>
    <select
      rounded
      outlined
      v-model="selectedVariant"
      @change="updateProductName"
      style="
        border: 1px solid #0b1aad;
        border-radius: 10px;
        color: rgba(75, 81, 98, 0.806);
      "
    >
      <label class="placeholder">Product Variants</label>
      <option value="iphone14promax256gb">iPhone 14 Pro Max 256GB</option>
      <option value="iphone14promax512gb">iPhone 14 Pro Max 512GB</option>
      <option value="iphone14promax1tb">iPhone 14 Pro Max 1TB</option>
    </select>
  </div>
  <div
    class="seleccionar"
    v-if="
      productName === 'iphone14pro' ||
      productName === 'iphone14pro256gb' ||
      productName === 'iphone14pro512gb' ||
      productName === 'iphone14pro128gb' ||
      productName === 'iphone14pro1tb'
    "
  >
    <p
      style="
        color: rgba(75, 81, 98, 0.806);
        margin-left: 30px;
        margin-bottom: 0px;
        margin-top: -30px;
      "
    >
      Product Variants:
    </p>
    <select
      rounded
      outlined
      v-model="selectedVariant"
      @change="updateProductName"
      style="
        border: 1px solid #0b1aad;
        border-radius: 10px;
        color: rgba(75, 81, 98, 0.806);
      "
    >
      <label class="placeholder">Product Variants</label>
      <option value="iphone14pro128gb">iPhone 14 Pro 128GB</option>
      <option value="iphone14pro256gb">iPhone 14 Pro 256GB</option>
      <option value="iphone14pro512gb">iPhone 14 Pro 512GB</option>
      <option value="iphone14pro1tb">iPhone 14 Pro 1TB</option>
    </select>
  </div>
  <div
    class="seleccionar"
    v-if="
      productName === 'iphone14plus' ||
      productName === 'iphone14plus256gb' ||
      productName === 'iphone14plus512gb' ||
      productName === 'iphone14plus128gb'
    "
  >
    <p
      style="
        color: rgba(75, 81, 98, 0.806);
        margin-left: 30px;
        margin-bottom: 0px;
        margin-top: -30px;
      "
    >
      Product Variants:
    </p>
    <select
      rounded
      outlined
      v-model="selectedVariant"
      @change="updateProductName"
      style="
        border: 1px solid #0b1aad;
        border-radius: 10px;
        color: rgba(75, 81, 98, 0.806);
      "
    >
      <label class="placeholder">Product Variants</label>
      <option value="iphone14plus128gb">iPhone 14 Plus 128GB</option>
      <option value="iphone14plus256gb">iPhone 14 Plus 256GB</option>
      <option value="iphone14plus512gb">iPhone 14 Plus 512GB</option>
    </select>
  </div>
  <div class="textBajo" style="display: flex; margin-left: 200px">
    <div style="flex: 1; width: 700px; height: 350px">
      <p
        class="p4"
        style="margin-left: 30px; margin-top: 30px; font-size: 28px"
      >
        <strong>
          Transform Unsold<br />
          Inventory into Revenue <br />Streams
        </strong>
      </p>
      <p
        class="interior"
        style="margin-left: 30px; margin-top: -10px; font-size: 17px"
      >
        Around 92% of retailers in the US face the
        <br />challenge of managing unsold inventory. <br />However, taking a
        strategic approach to rent or <br />sell this surplus stock in the
        second-hand <br />
        market can substantially impact your <br />business's performance.
      </p>
    </div>
    <img
      src="icons/imagen2.png"
      alt="Image"
      style="margin-left: -260px; margin-top: 50px; height: 250px; width: 450px"
    />
  </div>
  <div
    class="textBajo"
    style="display: flex; margin-left: 200px; margin-top: -20px"
  >
    <div style="flex: 1; width: 700px; height: 350px">
      <p
        class="p4"
        style="margin-left: 30px; margin-top: 30px; font-size: 28px"
      >
        <strong> Increase Customer <br />Retention </strong>
      </p>
      <p
        class="interior"
        style="margin-left: 30px; margin-top: -10px; font-size: 17px"
      >
        Launching rentals and subscriptions can
        <br />significantly boost customer retention and <br />
        loyalty. By offering these flexible options, <br />
        businesses create a stronger bond with <br />
        customers, encouraging them to stay engaged <br />
        and committed to the brand over time.
      </p>
    </div>
    <img
      src="icons/imagen3.png"
      alt="Image"
      style="margin-left: -260px; margin-top: 50px; height: 250px; width: 450px"
    />
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
      src="icons/logo-dog.png"
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
export default {
  created() {
    this.totalAmount = sessionStorage.getItem("totalAmount");
    this.productName = sessionStorage.getItem("productName");
  },

  data() {
    return {
      totalAmount: null,
      productName: null,
      sliderValue: 6, // Valor inicial del slider (correspondiente a 12 meses)
      model: null,

      ticks: [
        { label: "6 months", value: 0 },
        { label: "12 months", value: 1 },
        { label: "24 months", value: 2 },
      ],
    };
  },

  computed: {
    monthlyAmount() {
      return (this.totalAmount / this.sliderValue).toFixed(2); // Calcula el monto mensual
    },
  },
  methods: {
    updateProductName(event) {
      this.productName = event.target.value.toLowerCase();
      this.totalAmount = this.calculateTotalAmount();
    },
    calculateTotalAmount() {
      // Lógica para calcular el precio basado en el nombre del producto seleccionado
      // Por ejemplo:
      if (this.productName === "iphone15promax256gb") {
        return 1699; // Precio para iPhone 15 Pro Max 256GB
      } else if (this.productName === "iphone15promax1tb") {
        return 1999; // Precio para iPhone 15 Pro Max 1TB
      } else if (this.productName === "iphone15promax512gb") {
        return 1899;
      } else if (this.productName === "iphone15 128gb") {
        return 1099;
      } else if (this.productName === "iphone15 256gb") {
        return 1199;
      } else if (this.productName === "iphone15 512gb") {
        return 1399;
      } else if (this.productName === "iphone15pro128gb") {
        return 1399;
      } else if (this.productName === "iphone15pro256gb") {
        return 1499;
      } else if (this.productName === "iphone15pro512gb") {
        return 1599;
      } else if (this.productName === "iphone15plus128gb") {
        return 1299;
      } else if (this.productName === "iphone15plus256gb") {
        return 1399;
      } else if (this.productName === "iphone15plus512gb") {
        return 1599;
      } else {
        return 0; // Precio predeterminado o lógica adicional
      }
    },
    getImageUrl() {
      if (
        this.productName === "iphone15" ||
        this.productName === "iphone15 512gb" ||
        this.productName === "iphone15 256gb" ||
        this.productName === "iphone15 128gb" ||
        this.productName === "iphone15plus128gb" ||
        this.productName === "iphone15plus512gb"
      ) {
        return "icons/iphone15.jpg";
      } else if (
        this.productName === "iphone15promax1tb" ||
        this.productName === "iphone15promax512gb" ||
        this.productName === "iphone15promax256gb" ||
        this.productName === "iphone15pro256gb" ||
        this.productName === "iphone15pro128gb" ||
        this.productName === "iphone15pro512gb"
      ) {
        return "icons/iphone15proMax.jpg";
      } else if (
        this.productName === "iphone14promax1tb" ||
        this.productName === "iphone14promax512gb" ||
        this.productName === "iphone14promax256gb" ||
        this.productName === "iphone14pro256gb" ||
        this.productName === "iphone14pro128gb" ||
        this.productName === "iphone14pro512gb"
      ) {
        return "icons/iphone14proMax.jpg";
      } else if (
        this.productName === "iphone14 128gb" ||
        this.productName === "iphone14 512gb" ||
        this.productName === "iphone14 256gb" ||
        this.productName === "iphone14plus256gb" ||
        this.productName === "iphone14plus128gb" ||
        this.productName === "iphone14plus512gb"
      ) {
        return "icons/iphone14.jpg";
      }
    },
  },
};
</script>

<style>
.seleccionar {
  margin-left: 320px;
  width: 300px;
  margin-top: -10px;
}
.interior {
  color: rgba(75, 81, 98, 0.806);
}

.textBajo {
  border: 1px solid #d1d5e2;
  border-radius: 20px;
  background-color: #f8f9fb;
  box-shadow: 0px 10px 20px rgba(48, 63, 119, 0.06),
    0px 2px 6px rgba(48, 66, 120, 0.06), 0px 0px 1px rgba(48, 66, 120, 0.06);
  padding: 6px;
  width: 900px; /* Para que el ancho se ajuste automáticamente al contenido */
  margin-left: 150px;
  margin-top: -90px;
  margin: 50px;
}
.h4 {
  margin-bottom: 5px; /* Reduce el margen inferior */
}
.custom-slider {
  margin-left: 220px;
  width: 350px; /* Reducción de la altura de la barra */
}
</style>
./LastSearches.vue
