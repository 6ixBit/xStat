<template>
    <div>
        <p>Choose a league: {{ selected }}</p>
        <b-form-select v-model="selected" :options="childValue">
            <template v-slot:first>
                <b-form-select-option :value="null" disabled>-- Select a league --</b-form-select-option>
            </template>
        </b-form-select>
        <!--<b-form-select v-model="selected" :options="options" size="sm" class="mt-3"></b-form-select>-->
  </div>
</template>

<script>
export default {
    props: ["childValue"],
    data(){
        return {
            selected: ""
        }
    }
}
</script>