<template>
    <v-card>
        <v-card-actions class="justify-center" style="height: 24rem;">
            <div>
                <v-file-input v-model="file" label="Upload File" prepend-icon="" multiple outlined color="primary"
                    accept="text/xlsx"></v-file-input>
                <p>accepted file: .xlsx</p>
            </div>
        </v-card-actions>
    </v-card>
</template>

<script>

</script>

<style></style>