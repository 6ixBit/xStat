<template>
  <div>
    <b-card
      no-body
      style="max-width: 20rem;"
      img-src="https://placekitten.com/380/200"
      img-alt="Image"
      img-top
    >
      <template v-slot:header>
        <h4 class="mb-0">De Bruyne</h4>
      </template>

      <b-list-group flush>
        <b-list-group-item>Goals: 10</b-list-group-item>
        <b-list-group-item>Dapibus ac facilisis in</b-list-group-item>
        <b-list-group-item>Vestibulum at eros</b-list-group-item>
      </b-list-group>

      <b-card-body>
        <a href="#" class="card-link">Card link</a>
        <a href="#" class="card-link">Another link</a>
      </b-card-body>

    </b-card>
  </div>
</template>
