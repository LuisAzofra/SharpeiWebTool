<template>
  <div
    class="image-container"
    style="
      position: relative;
      flex: 0 0 calc(50% - 20px);
      margin-bottom: -30px;
      margin-right: 40px;
    "
  >
    <img
      src="icons/(HIDDEN TO MAKE CODE PUBLIC)"
      alt="Logo"
      style="
        width: 1182px;
        border-radius: 20px;
        border: 1px solid #d1d5e2;
        left: 30px;
        margin-top: 0px;
        object-fit: cover;
        object-position: center;
      "
    />
  </div>

  <h4 class="text-center" style="margin-bottom: 5px">
    <strong>Calculate business potential with Sharpei <br /></strong>
    <span class="text-secondary">
      <strong>and new consumption models in your e-commerce</strong>
    </span>
  </h4>

  <q-btn
    outline
    no-caps
    round
    color="secondary"
    class="custom-btn"
    @click="onClick"
    style="position: fixed; bottom: 20px; right: 2px"
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
  <div class="content-wrapper" style="justify-content: center">
    <div class="container">
      <div class="slider-wrapper" style="position: relative">
        <div
          class="slider-container"
          style="position: relative; margin-top: -10px"
        >
          <h3
            class="slider-title text-center text-secondary"
            style="
              font-size: 18px;
              position: absolute;
              top: -10px;
              left: 50%;
              transform: translateX(-50%);
            "
          >
            <b>Input Section</b>
          </h3>
          <p
            id="rentals-text"
            class="slider-title2 text-center"
            style="
              color: #d1d5e2;
              font-size: 14px;
              position: absolute;
              top: 50px;
              left: 50%;
              transform: translateX(-50%);
            "
          >
            Adjust Parameters According to <br />Your Business Data
          </p>

          <div class="column" style="margin-left: 10px">
            <div class="slider-group">
              <h4 class="slider-title" style="margin-top: 80px">Industry</h4>
              <div class="textLow">
                <q-select
                  v-model="sector"
                  :options="sectorOptions"
                  color="secondary"
                  text-color="secondary"
                  class="custom-select"
                  placeholder="Choose a Industry"
                  style="text-align: left"
                />
              </div>
            </div>
            <div class="slider-group">
              <h5 class="slider-title" style="margin-top: 73px">
                Number of Orders: {{ formatNumber(sliderValues[1]) }}
              </h5>
              <q-slider
                v-model="sliderValues[1]"
                color="secondary"
                style="height: 24px; width: 200px"
                :min="10"
                :max="10000"
              />
              <div class="input-container" style="margin-top: -5px">
                <span class="input-label">Or insert a value here: </span>
                <div class="number-input-container">
                  <input
                    type="text"
                    v-model="editedSliderValue[1]"
                    @change="updateSliderValue(1)"
                    style="
                      border: none;
                      border-bottom: 1px solid var(--q-color-secondary);
                      background: none;
                      outline: none;
                      width: 50px;
                      font-size: 13px;
                      font-weight: bold;
                      color: var(--q-color-secondary);
                      margin-top: -5px;
                      margin-left: -7px;
                    "
                  />
                </div>
              </div>
              <span class="input-helper-text">
                (Press Enter to save the new value)
              </span>
            </div>
          </div>
          <div class="column" style="margin-right: 10px">
            <div class="slider-group">
              <h5 class="slider-title" style="margin-top: 85px">
                Average Product Cost: ${{ formatNumber(sliderValues[0]) }}
              </h5>
              <q-slider
                v-model="sliderValues[0]"
                color="secondary"
                style="height: 24px; width: 200px"
                :min="10"
                :max="10000"
              />
              <div class="input-container" style="margin-top: -5px">
                <span class="input-label">Or insert a value here:</span>
                <div class="number-input-container">
                  <input
                    type="text"
                    v-model="editedSliderValue[0]"
                    @change="updateSliderValue(0)"
                    style="
                      border: none;
                      border-bottom: 1px solid var(--q-color-secondary);
                      background: none;
                      outline: none;
                      width: 50px;
                      font-size: 13px;
                      font-weight: bold;
                      color: var(--q-color-secondary);
                      margin-top: -5px;
                      margin-left: -7px;
                    "
                  />
                </div>
              </div>
              <span class="input-helper-text">
                (Press Enter to save the new value)
              </span>
            </div>
            <div class="slider-group">
              <h5 class="slider-title" style="margin-top: 33px">
                Average Retail Price: ${{ formatNumber(sliderValues[2]) }}
              </h5>
              <q-slider
                v-model="sliderValues[2]"
                color="secondary"
                style="height: 24px; width: 200px"
                :min="10"
                :max="10000"
              />
              <div class="input-container" style="margin-top: -5px">
                <span class="input-label">Or insert a value here:</span>
                <div class="number-input-container">
                  <input
                    type="text"
                    v-model="editedSliderValue[2]"
                    @change="updateSliderValue(2)"
                    style="
                      border: none;
                      border-bottom: 1px solid var(--q-color-secondary);
                      background: none;
                      outline: none;
                      width: 50px;
                      font-size: 13px;
                      font-weight: bold;
                      color: var(--q-color-secondary);
                      margin-top: -5px;
                      margin-left: -7px;
                    "
                  />
                </div>
              </div>
              <span class="input-helper-text">
                (Press Enter to save the new value)
              </span>
            </div>
            <div class="slider-group" style="margin-top: 29px">
              <!-- Submit Button -->
              <q-btn
                color="primary"
                @click="submitForm"
                text-color="secondary"
                no-caps
                label="Submit"
                class="submit-btn"
                style="
                  margin-top: 10px;
                  margin-left: -100px;
                  border: 1px solid #0b1aad;
                  border-radius: 20px;
                  background-color: #f8f9fb;
                  margin-bottom: 2px;
                "
              >
              </q-btn>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="container" style="flex: 0 0 calc(50% - 20px)">
      <div
        class="slider-container2"
        style="
          margin-top: 10px;
          display: flex;
          flex-direction: column;
          align-items: center;
        "
      >
        <h3
          class="slider-title text-center text-secondary"
          style="font-size: 18px; margin-bottom: -5px; margin-top: -10px"
        >
          <b>Profit Calculator</b>
        </h3>
        <p
          id="rentals-text"
          class="slider-title2 text-center"
          style="color: #d1d5e2; margin-bottom: -20px; margin-top: -5px"
        >
          Considering <b style="font-size: 16px">{{ RentalsBeforeSale }}</b>
          <span v-if="RentalsBeforeSale == 1"> rental per product</span
          ><span v-else> rentals per garment</span> before selling it
          <br />
          (Depends on the Product Condition)
        </p>
        <div style="display: flex; justify-content: space-between; width: 100%">
          <div
            class="column"
            style="
              margin-right: 20px;
              display: flex;
              flex-direction: column;
              align-items: center;
            "
          >
            <div class="slider-item">
              <h5
                class="slider-title text-center"
                style="font-size: 18px; margin-top: 30px"
              >
                <b>Number of Rentals:</b>
              </h5>
              <h5
                class="slider-value text-center"
                style="font-size: 18px; margin-top: -25px"
              >
                {{ rentalDevices }}
              </h5>
            </div>

            <div class="slider-item">
              <h5
                class="slider-title text-center"
                style="font-size: 18px; margin-top: -20px"
              >
                <b>Total Contract Value:</b>
              </h5>
              <h5
                class="slider-value text-center"
                style="font-size: 18px; margin-top: -25px"
              >
                ${{ formatNumber(totalContractValue, false) }}
              </h5>
            </div>
            <div class="slider-item">
              <h5
                class="slider-title text-center"
                style="font-size: 18px; margin-top: -20px"
              >
                <b>Additional Profits with Sharpei </b>
              </h5>
              <div
                class="flex-container"
                style="justify-content: center; align-items: center"
              >
                <h5
                  class="slider-value text-center"
                  style="font-size: 13px; margin-top: -35px; color: #16a81c"
                >
                  +${{ formatNumber(EarningComparedToNormalSale, false) }}
                </h5>

                <svg class="arrows">
                  <path class="a1" d="M0 0 L30 32 L60 0"></path>
                  <path class="a2" d="M0 20 L30 52 L60 20"></path>
                  <path class="a3" d="M0 40 L30 72 L60 40"></path>
                  <path class="a3" d="M0 40 L30 72 L60 40"></path>
                </svg>
              </div>
              <div
                style="display: flex; align-items: center; position: relative"
              >
                <h5
                  class="slider-value"
                  style="
                    font-size: 18px;
                    margin-top: 15px;
                    position: absolute;
                    left: 50%;
                    color: #0b1aad;
                    transform: translateX(-50%);
                    margin-left: 62px;
                  "
                >
                  ${{ formatNumber(rentToOwnProfit, false) }}
                </h5>
                <h5
                  class="slider-value"
                  style="
                    font-size: 18px;
                    margin-top: 15px;
                    position: absolute;
                    transform: translateX(50%);
                    margin-right: 55px;
                    right: 50%;
                  "
                >
                  ${{ formatNumber(directSalesIncome, false) }}
                </h5>
              </div>
              <div
                style="
                  display: flex;
                  align-items: center;
                  position: relative;
                  margin-top: -35px;
                "
              >
                <p style="font-size: 9px; margin-left: 39px; margin-top: 38px">
                  (Current Profit)
                </p>

                <p
                  style="
                    font-size: 9px;
                    color: #0b1aad;
                    margin-left: 60px;
                    margin-top: 38px;
                  "
                >
                  (With Sharpei)
                </p>
              </div>
            </div>
          </div>
          <div
            class="column"
            style="display: flex; flex-direction: column; align-items: center"
          >
            <div class="slider-item">
              <h5
                class="slider-title text-center"
                style="font-size: 18px; margin-top: 30px"
              >
                <b>Average Rental Time:</b>
              </h5>
              <h5
                class="slider-value text-center"
                style="font-size: 18px; margin-top: -25px"
              >
                {{ averageRentalTime }} months
              </h5>
            </div>
            <div class="slider-item" style="text-align: center">
              <h5
                class="slider-title"
                style="font-size: 18px; margin-top: -20px"
              >
                <b>Revenue rental + reselling:</b>
              </h5>
              <h5
                class="slider-value"
                style="font-size: 18px; margin-top: -25px"
              >
                ${{ formatNumber(rentToOwnProfit, false) }}
              </h5>
            </div>
            <div class="slider-item" style="text-align: center">
              <h5
                class="slider-title"
                style="font-size: 18px; margin-top: -20px"
              >
                <b>Revenue compared with normal sale:</b>
              </h5>
              <h5
                class="slider-value"
                style="font-size: 18px; margin-top: -4px"
              >
                {{ revenueComparedToNormalSale }}%
              </h5>
            </div>
          </div>
        </div>

        <div
          style="
            display: flex;
            justify-content: space-between;
            margin-top: -10px;
          "
        >
          <a href="https://www.gosharpei.com/contact" target="_blank">
            <q-btn
              no-caps
              color="secondary"
              rounded
              square
              label="Contact Sales"
              class="button-bold2"
              style="
                border-radius: 7px;
                margin-top: 20px;
                margin-left: 10px;
                font-size: 16px !important;
                font-family: 'DM Sans Placeholder', sans-serif;
                font-weight: bold;
              "
            />
          </a>
          <a href="https://www.gosharpei.com/about-us" target="_blank">
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
                font-weight: bold;
              "
            />
          </a>
        </div>
        <p
          class="slider-title2 text-center"
          style="
            color: #d1d5e2;
            font-size: 12px;
            margin-bottom: -15px;
            margin-top: 5px;
          "
        >
          *Please note that the calculations provided are estimations and may
          vary*
        </p>
      </div>
    </div>
  </div>
</template>

<script>
import { defineComponent } from "vue";

export default defineComponent({
  name: "Depreciation-Calculator",
  data() {
    return {
      filter: "",
      sliderValues: [1000, 2000, 2000], // Initial slider values
      editedSliderValue: [0, 0, 0], // Edited slider values
      sector: "Select an Industry",
      sectorOptions: ["Fashion", "Consumer Electronics", "Mobility"],
      rentalDevices: 0,
      averageContract: 0,
      totalContractValue: 0,
      residualCost: 0,
      recommendedPrice: 0,
      directSalesProfit: 0,
      directSalesIncome: 0,
      averageRentalTime: 0,
      rentToOwnProfit: 0,
      rentToOwnIncome: 0,
      temporalidad: 18,
      buyout: 0,
      rentProfit: 0,
      rentIncome: 0,
      revenueComparedToNormalSale: 0,
      EarningComparedToNormalSale: 0,
      RentalsBeforeSale: 0,
    };
  },

  methods: {
    onClick() {
      // Logic for button click
    },
    editSliderValue(index) {
      let newValue = prompt("Enter a new value:");
      if (!isNaN(newValue) && newValue !== null) {
        this.sliderValues[index] = parseInt(newValue);
        this.editedSliderValue[index] = parseInt(newValue);
      }
    },

    updateSliderValue(index) {
      let newValue = parseInt(this.editedSliderValue[index]);
      if (!isNaN(newValue)) {
        this.sliderValues[index] = newValue;
      } else {
        this.editedSliderValue[index] = this.sliderValues[index];
      }
    },

    calculateValues() {
      //HIDDEN TO MAKE CODE PUBLIC

      // Updated calculation formulas
      //HIDDEN TO MAKE CODE PUBLIC
      
      //Affected by RentalsBeforeSale
       //HIDDEN TO MAKE CODE PUBLIC

      // Calcular la tasa de depreciación
       //HIDDEN TO MAKE CODE PUBLIC

      //Affected by RentalsBeforeSale
       //HIDDEN TO MAKE CODE PUBLIC

      // Formatear los valores numéricos
      this.rentalDevices = this.formatNumber(this.rentalDevices);
      this.averageRentalTime =
        this.averageRentalTime % 1 === 0
          ? `${this.averageRentalTime} `
          : this.averageRentalTime.toFixed(2);
      this.averageContract = this.formatNumber(this.averageContract);
      this.totalContractValue = this.formatNumber(this.totalContractValue);
      this.buyout = this.formatNumber(this.buyout);
      this.rentToOwnProfit = this.formatNumber(this.rentToOwnProfit);
      this.revenueComparedToNormalSale =
        this.revenueComparedToNormalSale.toFixed(2);
       //EXTRA DATA HIDDEN TO MAKE CODE PUBLIC
    },
    formatNumber(number, isDecimal) {
      if (isDecimal) {
        return number.toLocaleString("en", {
          minimumFractionDigits: 2,
          maximumFractionDigits: 2,
        });
      } else {
        return number.toLocaleString("en", {
          minimumFractionDigits: 0,
          maximumFractionDigits: 0,
        });
      }
    },
    submitForm() {
      // Verificar si se ha seleccionado una industria
      if (this.sector === "Select an Industry") {
        // Seleccionar automáticamente 'Consumer Electronics'
        this.sector = "Consumer Electronics";
      }

      // Call calculateValues function to update the values
      this.calculateValues();

      const secondContainer =
        document.querySelectorAll(".slider-container2")[0];

      // Hacer scroll hasta el segundo contenedor
      secondContainer.scrollIntoView({
        behavior: "smooth", // Scroll suave
        block: "start", // Alinea el inicio del contenedor con el inicio del área visible del elemento que hace scroll
      });

      // Logic for submitting the form
      this.$q.loading.show({
        message: "Submitting...",
        messageColor: "secondary",
        backgroundColor: this.$q.theme.secondary,
      });
      setTimeout(() => {
        this.$q.loading.hide();
      }, 2000);
    },
  },
});
</script>

<style scoped>
.text-center {
  text-align: center; /* Centra el texto horizontalmente */
}
.container {
  position: relative;
}
.image-container {
  margin-top: 30px;
  margin-left: 30px;
}
.button-bold {
  font-weight: bold !important;
}
.text-secondary {
  color: var(--q-color-secondary);
}
.content-wrapper {
  display: flex;
  align-items: flex-start; /* Alinea los contenedores desde la parte superior */
  flex-wrap: wrap; /* Envuelve los contenedores si no caben en una sola fila */
}
.slider-wrapper {
  margin-top: 20px; /* Space between text and sliders */
}

.textLow {
  display: flex;
  align-items: center;
  justify-content: flex-start;
  height: 40px;
  max-width: 200px; /* Adjustable maximum width */
  border: 1px solid #d1d5e2;
  border-radius: 20px;
  background-color: #f8f9fb;
  box-shadow: 0px 10px 20px rgba(48, 63, 119, 0.06),
    0px 2px 6px rgba(48, 66, 120, 0.06), 0px 0px 1px rgba(48, 66, 120, 0.06);
  padding: 10px;
  margin-left: -5px;
}
.arrows {
  width: 12px; /* Ancho deseado */
  height: 8px; /* Alto deseado */
  position: absolute;
  overflow: visible; /* Evitar que las flechas se recorten */
  transform: rotate(270deg) scale(0.4); /* Rotar las flechas 270 grados y ajustar el tamaño */
  margin-top: 25px;
  margin-left: -20px;
}

.arrows path {
  stroke: #0b1aad;
  fill: transparent;
  stroke-width: 1px;
  animation: arrow 2s infinite;
  -webkit-animation: arrow 2s infinite;
}

@keyframes arrow {
  0% {
    opacity: 0;
  }
  40% {
    opacity: 1;
  }
  80% {
    opacity: 0;
  }
  100% {
    opacity: 0;
  }
}

@-webkit-keyframes arrow {
  0% {
    opacity: 0;
  }
  40% {
    opacity: 1;
  }
  80% {
    opacity: 0;
  }
  100% {
    opacity: 0;
  }
}

.arrows path.a1 {
  animation-delay: -1s;
  -webkit-animation-delay: -1s;
}

.arrows path.a2 {
  animation-delay: -0.5s;
  -webkit-animation-delay: -0.5s;
}

.arrows path.a3 {
  animation-delay: 0s;
  -webkit-animation-delay: 0s;
}

.slider-container {
  display: flex;
  justify-content: space-between;
  border: 1px solid #d1d5e2;
  border-radius: 20px;
  background-color: #f8f9fb;
  box-shadow: 0px 10px 20px rgba(48, 63, 119, 0.06),
    0px 2px 6px rgba(48, 66, 120, 0.06), 0px 0px 1px rgba(48, 66, 120, 0.06);
  padding: 20px;
  width: 550px; /* Auto-adjust width */
  margin-left: 30px;
  margin-bottom: 20px;
}
.slider-container2 {
  display: flex;
  justify-content: space-between;
  border: 1px solid #d1d5e2;
  border-radius: 20px;
  background-color: #f8f9fb;
  box-shadow: 0px 10px 20px rgba(48, 63, 119, 0.06),
    0px 2px 6px rgba(48, 66, 120, 0.06), 0px 0px 1px rgba(48, 66, 120, 0.06);
  padding: 20px;
  width: 600px; /* Auto-adjust width */
  margin-left: 30px;
  margin-right: 40px;
  margin-bottom: 20px;
}
.number-input-container {
  display: inline-block;
  background-color: white;
  border-radius: 10px;
  padding: 5px 10px;
  border: 1px solid #d1d5e2;
  margin-left: 5px;
}

.slider-group {
  margin-bottom: 10px; /* Space between slider groups */
}
.slider-group2 {
  margin-bottom: 10px; /* Space between slider groups */
}

.slider-group .slider-title {
  font-size: 14px; /* Slider title size */
  margin-bottom: 0px;
}

.selected-sector {
  background-color: white; /* White background */
  border: 1px solid #d1d5e2; /* Gray borders */
  border-radius: 3px; /* Rounded borders */
  padding: 5px; /* Inner space */
  margin-top: 5px; /* Adjust as needed */
}

q-slider {
  --q-slider-handle-color: var(--q-color-secondary); /* Slider ball color */
}
.image-container {
  display: flex;
  justify-content: center; /* Centra horizontalmente */
  margin-bottom: -30px;
}
.input-container {
  display: flex;
  align-items: center;
  margin-top: 5px; /* Adjust as needed */
}

.input-label {
  font-weight: bold;
  font-size: 12px; /* Reduced size */
  margin-left: 5px;
}

.input-helper-text {
  font-size: 10px; /* Reduced size */
  color: var(--q-color-secondary);
  margin-top: 5px; /* Adjust as needed */
  margin-left: 5px;
}

.submit-text {
  color: solid #0b1aad;
  margin: 0;
}

.submit-btn:hover {
  background-color: var(--q-color-secondary);
  color: white;
}

.submit-btn:focus {
  background-color: var(--q-color-secondary);
  color: white;
}
.flex-container {
  display: flex;
  align-items: center;
}

.text {
  margin-left: 5px; /* Ajusta el valor según sea necesario */
}
</style>
