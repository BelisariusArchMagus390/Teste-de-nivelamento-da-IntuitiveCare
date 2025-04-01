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
</script>

<template>
  <div>
    <h1>Buscar Operadora</h1>
    <input v-model="input_field" placeholder="Digite aqui o que quer buscar." />

    <select v-model="column_search">
      <option value="Registro_ANS">Registro ANS</option>
      <option value="CNPJ">CNPJ</option>
      <option value="Razao_Social">Razão social</option>
      <option value="Nome_Fantasia">Nome fantasia</option>
      <option value="Modalidade">Modalidade</option>
      <option value="Logradouro">Logradouro</option>
      <option value="Numero">Número</option>
      <option value="Complemento">Complemento</option>
      <option value="Bairro">Bairro</option>
      <option value="Cidade">Cidade</option>
      <option value="UF">UF</option>
      <option value="CEP">CEP</option>
      <option value="DDD">DDD</option>
      <option value="Telefone">Telefone</option>
      <option value="Fax">Fax</option>
      <option value="Endereco_eletronico">Endereco eletrônico</option>
      <option value="Representante">Representante</option>
      <option value="Cargo_Representante">Cargo do representante</option>
      <option value="Regiao_de_Comercializacao">Regiao de comercialização</option>
      <option value="Data_Registro_ANS">Data de registro do ANS</option>
    </select>

    <button @click="searchInformationTable">Buscar</button>
    
    <table border="1">
      <thead>
        <tr>
          <th v-for="(content, column) in result_search[0]" :key="column">{{ column }}</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(row, index) in result_search" :key="index">
          <td v-for="(content, column) in row" :key="column">{{ content }}</td>
        </tr>
      </tbody>
    </table>

  </div>
</template>

<style>
input {
  padding: 5px;
  margin-right: 10px;
}
</style>  