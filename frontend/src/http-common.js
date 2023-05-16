import axios from "axios";

export default axios.create({
  baseURL: "https://b97ffv5xi6.execute-api.us-west-2.amazonaws.com/default/cars/",
  headers: {
    "Content-type": "application/json"
  }
});
