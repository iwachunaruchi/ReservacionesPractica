<script setup>
import { RouterLink } from 'vue-router';
import { auth } from '@/stores/auth/auth';
const authStore = auth();
const handleLogout = async () => {
  await authStore.logout();
};
</script>
<template>
<nav class="navbar navbar-expand-lg bg-info">
                            <div class="container px-0">
                              <RouterLink to="/">
                                <img src="../assets/logo.png" alt="Geeks" width="80" />
                              </RouterLink>
                              <!-- Mobile view nav wrap -->
                              <div class="ms-auto d-flex align-items-center order-lg-3">
                                <div class="d-flex gap-2 align-items-center">
                                  <a href="#langaugeModal" class="text-inherit me-2" data-bs-toggle="modal">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" fill="currentColor" class="bi bi-globe text-gray-500" viewBox="0 0 16 16">
                                      <path
                                        d="M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8m7.5-6.923c-.67.204-1.335.82-1.887 1.855A8 8 0 0 0 5.145 4H7.5zM4.09 4a9.3 9.3 0 0 1 .64-1.539 7 7 0 0 1 .597-.933A7.03 7.03 0 0 0 2.255 4zm-.582 3.5c.03-.877.138-1.718.312-2.5H1.674a7 7 0 0 0-.656 2.5zM4.847 5a12.5 12.5 0 0 0-.338 2.5H7.5V5zM8.5 5v2.5h2.99a12.5 12.5 0 0 0-.337-2.5zM4.51 8.5a12.5 12.5 0 0 0 .337 2.5H7.5V8.5zm3.99 0V11h2.653c.187-.765.306-1.608.338-2.5zM5.145 12q.208.58.468 1.068c.552 1.035 1.218 1.65 1.887 1.855V12zm.182 2.472a7 7 0 0 1-.597-.933A9.3 9.3 0 0 1 4.09 12H2.255a7 7 0 0 0 3.072 2.472M3.82 11a13.7 13.7 0 0 1-.312-2.5h-2.49c.062.89.291 1.733.656 2.5zm6.853 3.472A7 7 0 0 0 13.745 12H11.91a9.3 9.3 0 0 1-.64 1.539 7 7 0 0 1-.597.933M8.5 12v2.923c.67-.204 1.335-.82 1.887-1.855q.26-.487.468-1.068zm3.68-1h2.146c.365-.767.594-1.61.656-2.5h-2.49a13.7 13.7 0 0 1-.312 2.5m2.802-3.5a7 7 0 0 0-.656-2.5H12.18c.174.782.282 1.623.312 2.5zM11.27 2.461c.247.464.462.98.64 1.539h1.835a7 7 0 0 0-3.072-2.472c.218.284.418.598.597.933M10.855 4a8 8 0 0 0-.468-1.068C9.835 1.897 9.17 1.282 8.5 1.077V4z" />
                                    </svg>
                                  </a>
                                  <div class="d-flex ">
                                    <div class="d-flex" v-if="authStore.rol == ''">
                                      <a  class="btn btn-outline-dark me-2">
                                      <RouterLink to="/login" class="no_link ">
                                        Iniciar Sesion
                                      </RouterLink>
                                      </a>
                                      <a  class="btn btn-dark d-none d-md-block">
                                        <RouterLink to="/register" class="no_link ">
                                          Registro
                                        </RouterLink>
                                      </a>
                                    </div>
                                    <div class="d-flex" v-else>
                                      <div class="me-2  no_link btn btn-light rounded-pill ">
                                        Bienvenido <a class="fst-italic no_link">{{authStore.rol}}</a>
                                      </div>
                                      <a>
                                          <RouterLink class="btn btn-dark d-none d-md-block rounded-pill me-2" to="/reservations">
                                            Reservaciones <i class="bi bi-houses-fill"></i>
                                          </RouterLink>
                                      </a>
                                      <a @click="handleLogout" class="btn btn-dark d-none d-md-block rounded-pill">
                                        <i class="bi bi-door-open-fill"></i>
                                      </a>
                                    </div>
                                  </div>
                                </div>
                              </div>
                              <div>
                                <!-- Button -->
                                <button
                                  class="navbar-toggler collapsed ms-2"
                                  type="button"
                                  data-bs-toggle="collapse"
                                  data-bs-target="#navbar-default"
                                  aria-controls="navbar-default"
                                  aria-expanded="false"
                                  aria-label="Toggle navigation">
                                  <span class="icon-bar top-bar mt-0"></span>
                                  <span class="icon-bar middle-bar"></span>
                                  <span class="icon-bar bottom-bar"></span>
                                </button>
                              </div>
                              <!-- Collapse -->
                              <div class="collapse navbar-collapse" id="navbar-default">
                                <ul class="navbar-nav mt-3 mt-lg-0 mx-auto">


                                </ul>
                              </div>
                            </div>
                          </nav>

                          <!-- Modal -->
                          <div class="modal fade" id="langaugeModal" tabindex="-1" aria-labelledby="langaugeModalLabel" aria-hidden="true">
                            <div class="modal-dialog modal-dialog-centered">
                              <div class="modal-content">
                                <div class="modal-body">
                                  <div class="d-flex justify-content-between align-items-center mb-4">
                                    <h3 class="modal-title" id="langaugeModalLabel">Choose a language</h3>
                                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                                  </div>
                                  <div class="row row-cols-2 row-cols-lg-3 g-2 g-lg-3">
                                    <a class="text-inherit fw-semibold active" href="#!">English</a>
                                    <a class="text-inherit fw-semibold" href="#!">Deutsch</a>
                                    <a class="text-inherit fw-semibold" href="#!">Español</a>
                                    <a class="text-inherit fw-semibold" href="#!">Français</a>
                                    <a class="text-inherit fw-semibold" href="#!">Indonesia</a>
                                    <a class="text-inherit fw-semibold" href="#!">Italiano</a>
                                    <a class="text-inherit fw-semibold" href="#!">日本語</a>
                                    <a class="text-inherit fw-semibold" href="#!">한국어</a>
                                    <a class="text-inherit fw-semibold" href="#!">Nederlands</a>
                                    <a class="text-inherit fw-semibold" href="#!">Polski</a>
                                    <a class="text-inherit fw-semibold" href="#!">Português</a>
                                    <a class="text-inherit fw-semibold" href="#!">Română</a>
                                    <a class="text-inherit fw-semibold" href="#!">Русский</a>
                                    <a class="text-inherit fw-semibold" href="#!">ภาษาไทย</a>
                                    <a class="text-inherit fw-semibold" href="#!">Türkçe</a>
                                    <a class="text-inherit fw-semibold" href="#!">Tiếng Việt</a>
                                    <a class="text-inherit fw-semibold" href="#!">中文(简体)</a>
                                    <a class="text-inherit fw-semibold" href="#!">中文(繁體)</a>
                                  </div>
                                </div>
                              </div>
                            </div>
                          </div>
                          

</template>
<style>
.no_link {

  text-decoration: none; /* Opcional: elimina el subrayado */
  color: inherit; /* Opcional: hereda el color del texto */
}

</style>