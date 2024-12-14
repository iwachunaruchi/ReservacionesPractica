<script setup>
import { ref } from "vue";
import { auth } from "@/stores/auth/auth";
import { reservation } from "@/stores/reservation/reservation";
import { useRouter } from "vue-router";
const authStore = auth();
const router = useRouter();
// Variables reactivas para los campos
const username = ref("");
const password = ref("");

// Función para manejar el login
const handleLogin = async() => {
  if (!username.value || !password.value) {
    alert("Por favor, completa todos los campos.");
    return;
  }

  console.log("Username:", username.value);
  console.log("Password:", password.value);

  // Aquí puedes hacer una llamada al backend para autenticar al usuario
  const response = await authStore.login(username.value, password.value);
  if(response == true){
    router.push("/");
  }
};
</script>
<template>
    <div class="d-flex justify-content-center align-items-center vh-100 bg-light">
      <div class="card p-4 shadow" style="width: 24rem;">
        <img loading="lazy" src="../../assets/logo_n.png"  sizes="(max-width: 300px) 100vw, 300px" class="w-100 edit_image" style="height: 256px; object-fit: cover" alt="">

        <h3 class="text-center mb-4 mt-2">Iniciar Sesión</h3>
        
        <!-- Formulario -->
        <form @submit.prevent="handleLogin">
          <!-- Username -->
          <div class="mb-3">
            <label for="username" class="form-label">Nombre de Usuario</label>
            <input
              type="text"
              id="username"
              class="form-control"
              v-model="username"
              placeholder="Ingresa tu usuario"
              required
            />
          </div>
          
          <!-- Password -->
          <div class="mb-3">
            <label for="password" class="form-label">Contraseña</label>
            <input
              type="password"
              id="password"
              class="form-control"
              v-model="password"
              placeholder="Ingresa tu contraseña"
              required
            />
          </div>
          
          <!-- Botón de Login -->
          <div class="d-grid">
            <button type="submit" class="btn btn-primary">Iniciar Sesión</button>
          </div>
        </form>
      </div>
    </div>
  </template>
  
  <style>
  /* Estilo opcional */
  body {
    background-color: #f8f9fa;
  }
  
  .card {
    border-radius: 10px;
  }
  </style>
  