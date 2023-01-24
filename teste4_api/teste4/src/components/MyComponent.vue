<template>
  <div>
    <input v-model="searchValue" placeholder="Search Value" />
    <input v-model="searchColumn" placeholder="Search Column" />
    <button @click="submitSearch">Search</button>
    <table>
        <thead>
            <tr>
                <th v-for="(value, key) in result[0]" :key="key">{{ key }}</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="row in result" :key="row.Registro_ANS">
                <td v-for="(value, key) in row" :key="key">{{ value }}</td>
            </tr>
        </tbody>
    </table>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      inputValue: '',
    }
  },
  methods: {
    async submitData() {
      const response = await axios.post('http://localhost:5000/submit', { data: this.inputValue });
      if(response.data.response === 'Data received') {
        console.log(response.data.data);
      }
    }
  }
}
</script>