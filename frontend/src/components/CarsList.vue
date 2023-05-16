<template>
  <div class="list row">
    <div class="col-md-8">
      <div class="input-group mb-3">
        <input type="text" class="form-control" placeholder="Search by pk"
          v-model="pk"/>
        <div class="input-group-append">
          <button class="btn btn-outline-secondary" type="button"
            @click="searchPk"
          >
            Search
          </button>
        </div>
      </div>
    </div>
    <div class="col-md-6">
      <h4>Cars List</h4>
      <ul class="list-group">
        <li class="list-group-item"
          :class="{ active: index == currentIndex }"
          v-for="(car, index) in cars"
          :key="index"
          @click="setActiveCar(car, index)"
        >
          {{ car.make }}
        </li>
      </ul>

    </div>
    <div class="col-md-6">
      <div v-if="currentCar">
        <h4>Car</h4>
        <div>
          <label><strong>Pk:</strong></label> {{ currentCar.pk }}
        </div>
        <div>
          <label><strong>Make:</strong></label> {{ currentCar.make }}
        </div>
        <div>
          <label><strong>Model:</strong></label> {{ currentCar.model }}
        </div>
        <div>
          <label><strong>Year:</strong></label> {{ currentCar.year }}
        </div>

        <router-link :to="'/cars/' + currentCar.pk" class="badge badge-warning">Edit</router-link>
      </div>
      <div v-else>
        <br />
        <p>Please click on a Car...</p>
      </div>
    </div>
  </div>
</template>

<script>
import CarDataService from "../services/CarDataService";

export default {
  name: "cars-list",
  data() {
    return {
      cars: [],
      currentCar: null,
      currentIndex: -1,
      pk: ""
    };
  },
  methods: {
    retrieveCars() {
      CarDataService.getAll()
        .then(response => {
          this.cars = response.data;
          console.log(response.data);
        })
        .catch(e => {
          console.log(e);
        });
    },

    refreshList() {
      this.retrieveCars();
      this.currentCar = null;
      this.currentIndex = -1;
    },

    setActiveCar(car, index) {
      this.currentCar = car;
      this.currentIndex = car ? index : -1;
    },
    
    searchPk() {
      console.log("search");
      CarDataService.get(this.pk)
        .then(response => {
          this.cars = [response.data];
          this.setActiveCar(null);
          console.log(response.data);
        })
        .catch(e => {
          console.log(e);
        });
    }
  },
  mounted() {
    this.retrieveCars();
  }
};
</script>

<style>
.list {
  text-align: left;
  max-width: 750px;
  margin: auto;
}
</style>
