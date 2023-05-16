import http from "../http-common";

class TutorialDataService {
  getAll() {
    console.log("Get all");
    return http.get("");
  }

  get(pk) {
    console.log("Get");
    return http.get(`${pk}/`);
  }

  create(data) {
    console.log("Create");
    return http.post("create/", data);
  }

  update(pk, data) {
    console.log("Update");
    return http.put(`update/${pk}/`, data);
  }

  delete(pk) {
    console.log("Delete");
    return http.delete(`delete/${pk}/`);
  }
}

export default new TutorialDataService();
