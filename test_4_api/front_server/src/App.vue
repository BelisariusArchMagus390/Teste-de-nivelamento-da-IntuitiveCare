<script setup>
import { ref } from "vue";

const input_field = ref("");
const column_search = ref("")
const result_search = ref([]);

const searchInformationTable = async () => {
  try {
    const api_response = await fetch(`http://127.0.0.1:8000/search?input_field=${input_field.value}&column_search=${column_search.value}`);
    // store the api_response
    result_search.value = await api_response.json();
  } catch (error) {
    console.error("Erro ao buscar dados:", error);
  }
};

const columns = ref([
  { title: "Registro ANS", value: "Registro_ANS" },
  { title: "CNPJ", value: "CNPJ" },
  { title: "Razão social", value: "Razao_Social" },
  { title: "Nome fantasia", value: "Nome_Fantasia" },
  { title: "Modalidade", value: "Modalidade" },
  { title: "Logradouro", value: "Logradouro" },
  { title: "Número", value: "Numero" },
  { title: "Complemento", value: "Complemento" },
  { title: "Bairro", value: "Bairro" },
  { title: "Cidade", value: "Cidade" },
  { title: "UF", value: "UF" },
  { title: "CEP", value: "CEP" },
  { title: "DDD", value: "DDD" },
  { title: "Telefone", value: "Telefone" },
  { title: "Fax", value: "Fax" },
  { title: "Endereço eletrônico", value: "Endereco_eletronico" },
  { title: "Representante", value: "Representante" },
  { title: "Cargo do representante", value: "Cargo_Representante" },
  { title: "Região de comercialização", value: "Regiao_de_Comercializacao" },
  { title: "Data de registro do ANS", value: "Data_Registro_ANS" }
]);

</script>

<template>
  <v-app>
    <div>
      <v-container>
        <!-- Cabeçalho fixo -->
        <v-row justify="center">
          <v-col cols="12" class="text-center">
            <v-card class="pa-3 title-card" elevation="6">
              <h1>Buscar registro cadastral</h1>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
      
      <v-container>
        <v-row justify="center" align="center" class="my-4">
          <v-col cols="12" md="4">
            <v-text-field
              v-model="input_field"
              placeholder="Digite aqui o que quer buscar."
              outlined
              dense
            ></v-text-field>
          </v-col>

          <v-col cols="12" md="4">
            <v-select
              v-model="column_search"
              :items="columns"
              label="Selecione pelo campo que quer buscar"
              outlined
              dense
            ></v-select>
          </v-col>

          <v-col cols="12" md="2" class="d-flex justify-center">
            <v-btn 
              @click="searchInformationTable" 
              class="custom-button"
            >
              Buscar
            </v-btn>
          </v-col>
        </v-row>
      </v-container>

      <v-container>
        <v-row justify="center">
          <v-col cols="12">
            <v-card v-if="result_search.length > 0" class="pa-4">
              <v-sheet class="table-container">
                <v-table border="1">
                  <thead>
                    <tr>
                      <th v-for="(content, column) in result_search[0]" :key="column">
                        {{ column.replace(/"/g, '') }}
                      </th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="(row, index) in result_search" :key="index">
                      <td v-for="(content, column) in row" :key="column">
                        {{ content.replace(/"/g, '') }}
                      </td>
                    </tr>
                  </tbody>
                </v-table>
              </v-sheet>
            </v-card>
          </v-col>
        </v-row>
      </v-container>

    </div>
  </v-app>
</template>

<style scoped>
.title-card {
  top: 20px;
  left: 50%;
  transform: translateX(-50%);
  width: 400px;
  z-index: 1000;
}
</style>