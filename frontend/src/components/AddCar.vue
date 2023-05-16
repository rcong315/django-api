<template>
  <div class="submit-form">
    <div v-if="!submitted">
      <div class="form-group">
        <label for="make">Make</label>
        <input
          type="text"
          class="form-control"
          id="make"
          required
          v-model="car.make"
          name="make"
        />
      </div>

      <div class="form-group">
        <label for="description">Model</label>
        <input
          type="text"
          class="form-control"
          id="model"
          required
          v-model="car.model"
          name="model"
        />
      </div>

      <div class="form-group">
        <label for="description">Year</label>
        <input
          type="number"
          class="form-control"
          id="year"
          required
          v-model="car.year"
          name="year"
        />
      </div>

      <button @click="saveCar" class="btn btn-success">Submit</button>
    </div>

    <div v-else>
      <h4>You submitted successfully!</h4>
      <button class="btn btn-success" @click="newCar">Add</button>
    </div>
  </div>
</template>

<script>
import CarDataService from "../services/CarDataService";

export default {
  name: "add-car",
  data() {
    return {
      car: {
        id: null,
        make: "",
        model: "",
        year: "",
        published: false
      },
      submitted: false
    };
  },
  methods: {
    saveCar() {
      var data = {
        make: this.car.make,
        model: this.car.model,
        year: this.car.year
      };

      CarDataService.create(data)
        .then(response => {
          this.car.pk = response.data.pk;
          console.log(response.data);
          this.submitted = true;
        })
        .catch(e => {
          console.log(e);
        });
    },
    
    newCar() {
      this.submitted = false;
      this.car = {};
    }
  }
};
</script>

<style>
.submit-form {
  max-width: 300px;
  margin: auto;
}
</style>
