<template>
  <div v-if="currentCar" class="edit-form">
    <h4>Car</h4>
    <form>
      <div class="form-group">
        <label for="make">Make</label>
        <input type="text" class="form-control" id="make"
          v-model="currentCar.make"
        />
      </div>
      <div class="form-group">
        <label for="model">Model</label>
        <input type="text" class="form-control" id="model"
          v-model="currentCar.model"
        />
      </div>
      <div class="form-group">
        <label for="year">Year</label>
        <input type="number" class="form-control" id="year"
          v-model="currentCar.year"
        />
      </div>

    </form>

    <button type="submit" class="badge badge-success mr-2"
      @click="updateCar"
    >
      Update
    </button>

    <button class="badge badge-danger"
      @click="deleteCar"
    >
      Delete
    </button>

    <p>{{ message }}</p>
  </div>

  <div v-else>
    <br />
    <p>Please click on a Car...</p>
  </div>
</template>

<script>
import CarDataService from "../services/CarDataService";

export default {
  name: "car",
  data() {
    return {
      currentCar: null,
      message: ''
    };
  },
  methods: {
    getCar(pk) {
        console.log(pk);
      CarDataService.get(pk)
        .then(response => {
          this.currentCar = response.data;
          console.log(response.data);
        })
        .catch(e => {
          console.log(e);
        });
    },

    updatePublished(status) {
      var data = {
        pk: this.currentCar.pk,
        make: this.currentCar.make,
        model: this.currentCar.model,
        year: this.currentCar.year,
        published: status
      };

      CarDataService.update(this.currentCar.pk, data)
        .then(response => {
          console.log(response.data);
          this.currentCar.published = status;
          this.message = 'The status was updated successfully!';
        })
        .catch(e => {
          console.log(e);
        });
    },

    updateCar() {
      CarDataService.update(this.currentCar.pk, this.currentCar)
        .then(response => {
          console.log(response.data);
          this.message = 'The car was updated successfully!';
        })
        .catch(e => {
          console.log(e);
        });
    },

    deleteCar() {
      CarDataService.delete(this.currentCar.pk)
        .then(response => {
          console.log(response.data);
          this.$router.push({ name: "cars" });
        })
        .catch(e => {
          console.log(e);
        });
    }
  },
  mounted() {
    this.message = '';
    this.getCar(this.$route.params.pk);
  }
};
</script>

<style>
.edit-form {
  max-width: 300px;
  margin: auto;
}
</style>
