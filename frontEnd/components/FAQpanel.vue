<template>
    <v-container>
        <v-expansion-panels>
            <v-expansion-panel v-for="(faq, index) in faqs" :key="index">
                <v-expansion-panel-header>
                    <b>{{ faq.question }}</b>
                </v-expansion-panel-header>
                <v-expansion-panel-content>
                    {{ faq.answer }}
                </v-expansion-panel-content>
            </v-expansion-panel>
        </v-expansion-panels>
    </v-container>
</template>
  
<script>
export default {
    data() {
        return {
            faqs: [
                { question: 'Who are you?', answer: 'A group of FYP students who working on deploying an open-source machine learning model on the web for anomaly detection on transactional data.' },
                { question: 'Is my data safe?', answer: 'We have no log policy, we do not store any of your data so it is safe.' },
                { question: 'What is your detection accuracy?', answer: 'Currently our accuracy is 95%.' },
                { question: 'How do I generate my result?', answer: 'Just upload your excel file onto our "Analyse" page.' },
            ]
        }
    }
}
</script>