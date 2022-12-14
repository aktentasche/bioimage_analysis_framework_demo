<template>
  <q-page class="row items-center justify-evenly">
    <div>
      <q-file
        v-model="image_original"
        label="Pick one file"
        filled
        style="max-width: 300px"
        @update:model-value="imageChanged()"
      ></q-file>
    </div>
    <div>
      <img :src="image_original_url" :alt="image_original_url" />
      <img :src="image_detect_ridges_url" :alt="image_detect_ridges_url" />
    </div>
  </q-page>
</template>

<script setup lang="ts">
import { ref } from 'vue';

import {
  DefaultService,
  Body_detect_ridges_detect_ridges_post
} from 'src/generated/index';

const image_original = ref(null);
const image_original_url = ref('');
const image_detect_ridges_url = ref('');

async function imageChanged() {
  if (image_original.value) {
    image_original_url.value = URL.createObjectURL(image_original.value);

    // detect ridges
    const post_blob: Body_detect_ridges_detect_ridges_post = {
      file: image_original.value
    };

    await DefaultService.detectRidgesDetectRidgesPost(post_blob).then(
      (response_blob) => {
        const blob_obj = new Blob([response_blob], { type: 'image/png' });
        console.log(response_blob);

        image_detect_ridges_url.value = URL.createObjectURL(blob_obj);
      }
    );
  }
}
</script>
