import axios from "axios";

// Crear instancia de Axios
const axiosClient = axios.create({
  baseURL: import.meta.env.URL_BACK, // URL base del backend
  timeout: 10000, // Tiempo máximo de espera por solicitud
  headers: {
    "Content-Type": "application/json",
  },
});

// Interceptor para manejar errores
axiosClient.interceptors.response.use(
  (response) => response, // Retorna la respuesta si es exitosa
  (error) => {
    if (error.response) {
      // Errores de respuesta del servidor
      console.error("Error de API:", error.response.data);
      return Promise.reject(error.response.data);
    } else if (error.request) {
      // Errores sin respuesta (por ejemplo, problemas de red)
      console.error("Error de red:", error.request);
      return Promise.reject({ error: "No se pudo conectar al servidor" });
    } else {
      // Otros errores
      console.error("Error:", error.message);
      return Promise.reject({ error: error.message });
    }
  }
);

export default axiosClient;
