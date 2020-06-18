<template>
  <v-app style="overflow-x: hidden;">
    <v-app-bar 
    clipped
    fixed
    app>
      <v-spacer></v-spacer>
      <v-toolbar-title>Упраления типовой инфраструктурой (ТИОФВ)</v-toolbar-title>
      <v-spacer></v-spacer>
      <!-- <v-btn color="primary" dark @click.stop="null">
        Информация
      </v-btn> -->
    </v-app-bar>
    <v-navigation-drawer 
        permanent
        fixed 
        width="22%"
        style="top: 64px; heigth: 100vh; max-height: calc(100% - 111px)"
        absolute
        v-model="value">
        
        <v-card
          height="100%"
        >
          <v-list
            v-if="getListPatterns == null"
            height="100%"
          >829
            <v-list-item
              style="margin: auto"
              height="100%"
            >
              <v-list-item-title height="100%" class="text-center">Здесь пока ничего нет</v-list-item-title>
            </v-list-item>
          </v-list>
          <v-list
            v-else
          > 
            <v-list-item
                style="margin: auto"
                height="100%"
              >
              <v-list-item-title height="100%" class="text-center">Сохраненные образы:</v-list-item-title>
            </v-list-item>
            <v-list-group
              prepend-icon="mdi-play-box-multiple"
              :value="false"
              nav
              v-for="item in getListPatterns"
              :key="item.name"
              style="overflow-y: auto; heigth: fit-content;"
            > 
              <template v-slot:activator>
                <v-list-item>
                  <v-list-item-content>
                    <v-list-item-title v-text="item.name"></v-list-item-title>
                    
                  </v-list-item-content>
                  <v-btn color="primary" title="Сделать образ активным"  dark icon @click.stop="run(item)">
                    <v-icon color="success" v-text="'mdi-play'"></v-icon> 
                  </v-btn>
                  <v-btn color="primary" class="ml-2" title="Удалить образ"  dark icon @click.stop="deleteItem(item)">
                    <v-icon color="error" v-text="'mdi-delete'"></v-icon> 
                  </v-btn>
                </v-list-item>
              </template>
              <v-divider></v-divider>
              <div class="param" style="margin-left: 30px; color: black">
                Параметры образа:
              </div>
              <div class="param"
                v-for="(param, key) in item"
                :key="key"
                v-if="key !== 'name' && key !== 'version'"
              >
                <!-- <div style="display: flex; ">  -->
                  <v-list-item-icon style="margin: 3px 10px 3px 40px">
                    <v-icon v-text="'mdi-cog-box'"></v-icon> 
                  </v-list-item-icon>
                  <span style="word-wrap: break-word;">{{convertKey(key) + ': ' + getBufName(key, param)}}</span>
                <!-- </div> -->
              </div>
            </v-list-group>
          </v-list>
        </v-card>
      </v-navigation-drawer>
    <!-- <v-main style="margin: 64px 0px 48px 20%; width: 78%; overflow-y: auto;"> -->
      <!-- <v-container> -->
        <Content/>
      <!-- </v-container> -->
    <!-- </v-main> -->

    <v-footer app padless>
      <v-col
        class="text-center"
        cols="12"
      >
        {{ new Date().getFullYear() }} — <strong>Strashioff LLC</strong>
      </v-col>
    </v-footer>
  </v-app>
</template>

<script>
import { mapGetters, mapActions }from 'vuex'
import Content from './Content'
import {eventBus} from '../main';

export default {
  name: 'Main',
  data () {
    return {
      value: true
    }
  },
  components: {
    Content
  },
  computed: {
    ...mapGetters('templates',['getListPatterns', 'getBufName'])
  },
  methods: {
    ...mapActions('templates', ['deleteParam']),
    convertKey (key) {
      if (key == 'db') {
        return "СУБД"
      } else if (key == 'lang') {
        return 'Язык'
      } else if (key == 'path') {
        return 'Путь проекта'
      } else if (key == 'interface') {
        return 'Интерфейс'
      } else if (key == 'option') {
        return 'Опции'
      } else if (key == 'password') {
        return 'Пароль'
      } else if (key == 'path') {
        return 'Путь проекта'
      } else if (key == 'path') {
        return 'Путь проекта'
      }
    },
    run (item) {
      eventBus.$emit('elem', item)
    },
    deleteItem (item) {
      this.deleteParam(item)
    }
  }
}
</script>

<style lang="scss" scoped>
  .param {
    height: 30px;
    line-height: 30px;
    display: flex;
    width: inherit;
  }
</style>