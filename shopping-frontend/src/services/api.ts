import axios from "axios";

export const api = axios.create({
  baseURL: "http://192.168.18.170:8000", // ajuste conforme seu ambiente
  headers: {
    "Content-Type": "application/json",
  },
});
