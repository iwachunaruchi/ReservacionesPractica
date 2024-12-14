const BASE_URL = import.meta.env.VITE_API_URL
export const apiClient = {
    async get(endpoint) {
      try {
        const response = await fetch(`${BASE_URL}${endpoint}`, {
          method: "GET",
          headers: {
            "Content-Type": "application/json",
            
          },
        });
        if (!response.ok) {
          throw new Error(`Error en GET ${endpoint}: ${response.status}`);
        }
        const data = await response.json();
        return data;
      } catch (error) {
        console.error(error);
        throw error;
      }
    },
  
    async post(endpoint, data) {
      try {
        const response = await fetch(`${BASE_URL}${endpoint}`, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(data),
        });
        if (!response.ok) {
          throw new Error(`Error en POST ${endpoint}: ${response.status}`);
        }
        return await response.json();
      } catch (error) {
        console.error(error);
        throw error;
      }
    },
  
    async put(endpoint, data) {
      try {
        const response = await fetch(`${BASE_URL}${endpoint}`, {
          method: "PUT",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(data),
        });
        if (!response.ok) {
          throw new Error(`Error en PUT ${endpoint}: ${response.status}`);
        }
        return await response.json();
      } catch (error) {
        console.error(error);
        throw error;
      }
    },
  
    async delete(endpoint) {
      try {
        const response = await fetch(`${BASE_URL}${endpoint}`, {
          method: "DELETE",
          headers: {
            "Content-Type": "application/json",
          },
        });
        if (!response.ok) {
          throw new Error(`Error en DELETE ${endpoint}: ${response.status}`);
        }
        return await response.json();
      } catch (error) {
        console.error(error);
        throw error;
      }
    },
  };