<template>
  <div class="wrapper">
    <div class="content">
      <h1 style="text-align: center; margin: 20px 0px;">Конфигурация и запуск инфраструктуры</h1>
      <v-card class="fields-text">
          <v-text-field  v-model="name" required label="Назавние инфраструктур"
             :counter="150"></v-text-field>
          <v-text-field :disabled="name==''"  v-model="path" value="/home/" required label="Абсолютный путь до проекта с веб приложением"
             :counter="150"></v-text-field>
          <div v-if="path!==''">Приложение должно запускаться на порту 8080</div>
          <v-select v-model="lang" :items="param.lang" item-text="name"  item-value="par" attach label="Язык" ></v-select>
          <v-select  :disabled="lang==''" v-model="version"  :items="getVersion()" item-text="name"  item-value="par"  attach label="Версия языка"></v-select>
          <v-text-field v-if="lang=='python'" :disabled="name==''"  v-model="option" value="/home/" required label="Имя файла, например requirements.txt, для python (Если его нет, то оставить пустым)"
             :counter="150"></v-text-field>
          <v-select   v-model="db"  :items="param.db" item-text="label"  item-value="par" attach label="База данных" ></v-select>
          <div v-if="db=='postgres:12'">Перед тем как запустить инфраструктуру добавьте в свой проект адресс базы данных "postgres://db:3306"</div>
          <div v-if="db=='mariadb:10.3'">Перед тем как запустить инфраструктуру добавьте в свой проект адресс базы данных "mysql://db:3306")</div>
          <v-text-field  v-model="password" required label="Пароль"
             :counter="150"></v-text-field>
          <v-select v-model="interface" :items="param.interface" item-text="name" item-value="par" attach label="Интерфейс СУБД Adminer" ></v-select>
          <div v-if="interface">Adminer будет доступен на порту 8080</div>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn @click="clear">Очисть все поля</v-btn>
            <v-btn :disabled="name=='' || db=='' ||lang=='' || version=='' || password=='' || path==''" @click="save" title="Сохраняет конфигурацию и запускает инфраструктуру" >Сохранить и запустить</v-btn>
          </v-card-actions>
      </v-card>
    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex'
import {eventBus} from '../main';

export default {
  name: 'Content',
  data () {
    return {
      db: '',
      interface: false,
      lang: '',
      name: '',
      option: '',
      password: '',
      path: '/home/alex/',
      version: '',
      param: {
        db: [
          {
            par: "postgres:12",
            label: "PostgresSQL 12"
          },
          {
            par: "mariadb:10.3",
            label: "MariaDB 10.3"
          }
        ],
        lang: [
          {
            name: "PHP",
            par: 'php',
            version: ['5.6', '7.4']
          },
          {
            name: "Python",
            par: 'python',
            version: [
              {
                name: '3,8',
                par: '3.8'
              },
              {
                name: '3,7',
                par: '3.7'
              }
            ]
          },
          {
            name: "Node JS",
            par: 'node',
            version: ['12', '13']
          }
        ],
        interface: [
          {
            name: "Добавить",
            par: true,
          },
          {
            name: "Недобалять",
            par: false,
          },
        ]
      }
    }
  },
  computed: {
    getVersion () {
      return () => {
        let elem = this.param.lang.find(elem => 
          elem.par == this.lang
        )
        if (elem !== undefined) return elem.version
        return []
      }
    }
  },
  methods: {
    ...mapActions('templates', ['saveParam']),
    save () {
      this.saveParam ({
        db: this.db,
        interface: this.interface,
        lang: this.lang,
        name: this.name,
        option: this.option,
        password: this.password,
        path: this.path,
        version: this.version,
      })
      this.clear()
    },
    clear () {
      this.db = ''
      this.interface = ''
      this.lang = ''
      this.name = ''
      this.option = ''
      this.password = ''
      this.path = ''
      this.version = ''
    }
  },
  mounted() {
    eventBus.$on('elem', (data) => {
      this.db = data.db
      this.interface = data.interface
      this.lang = data.lang
      this.name = data.name
      this.option = data.option
      this.password = data.password
      this.path = data.path
      this.version = data.version
    })
  }
}
</script>

<style lang="scss" scoped>
  .wrapper {
    padding: 64px 100px 48px 20%; 
    width: 100%;
    height: 100%;
    overflow-x: auto;
    overflow-y: hidden;


    .content {
      width: 1200px;
      height: 100%;

      .fields-text {
        padding: 10px 5%;
        width: 100%;
        height: 100%;
      }
    }
  }
</style>