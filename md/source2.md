author:            Mehdi Chou.
summary:           Android
id:                android
categories:        mobile
environments:      dev
status:            tutorial
feedback link:


# Android : Développement Mobile

## Introduction

**Contenu:**

* [Qu'est-ce qu'Android?](#Introduction)
* [Pourquoi développer des applications pour Android?](#Pourquoi)
* [Versions Android](#versions)
* [Les défis du développement d'applications Android](#défis)
* [En savoir plus](#learnmore)


> Android est un système d'exploitation et une plate-forme de programmation développés par Google pour les téléphones mobiles et autres appareils mobiles, tels que les tablettes.

### Qu'est-ce qu'Android?

Android est un système d'exploitation et une plate-forme de programmation développés par Google pour les téléphones mobiles et autres appareils mobiles, tels que les tablettes. Il peut fonctionner sur de nombreux appareils de différents fabricants. Android comprend un kit de développement logiciel (SDK) qui vous aide à écrire du code original et à assembler des modules logiciels pour créer des applications pour les utilisateurs d'Android. Android fournit également un marché pour distribuer des applications. Au total, Android représente un écosystème pour les applications mobiles.
![Android pour téléphones mobiles](images/dg_android_smartphone_apps.png)

### Pourquoi développer des applications pour Android?


Les développeurs créent des applications pour diverses raisons. Ils peuvent être amenés à répondre aux besoins de l'entreprise ou à créer de nouveaux services ou entreprises, ou encore à proposer des jeux et d'autres types de contenu aux utilisateurs. Les développeurs choisissent de développer pour Android afin de toucher la majorité des utilisateurs d'appareils mobiles.

### Plate-forme la plus populaire pour les applications mobiles

Android est la plate-forme mobile la plus populaire au monde et alimente des centaines de millions d'appareils mobiles dans plus de 190 pays. Il possède la plus grande base installée de toutes les plates-formes mobiles et continue de croître rapidement. Chaque jour, un autre million d'utilisateurs allume ses appareils Android pour la première fois et commence à rechercher des applications, des jeux et d'autres contenus numériques. ![Applications populaires sur Android](images/dg_app_examples.png)

### Meilleure expérience pour les utilisateurs d'applications

Android fournit une interface utilisateur à écran tactile pour l’interaction avec les applications. L'interface utilisateur d'Android est principalement basée sur la manipulation directe. Les personnes utilisent des gestes tactiles tels que glisser, taper et pincer pour manipuler des objets à l'écran. En plus du clavier, il existe un clavier à l'écran personnalisable pour la saisie de texte. Android peut également prendre en charge les contrôleurs de jeu et les claviers physiques de grande taille connectés par Bluetooth ou par USB. ![Icônes d'application sur l'écran d'accueil (à gauche), lecture de musique (au centre) et affichage des widgets (à droite)](images/dg_user_interfaces_widgets.png)

L'écran d'accueil Android peut contenir plusieurs sous-fenêtres de _app icons_, qui lancent leurs applications associées. Les volets de l'écran d'accueil peuvent également contenir des widgets _app, qui affichent en direct des contenus mis à jour automatiquement, tels que la météo, la boîte de réception de l'utilisateur ou un message de nouvelles. Android peut également lire du contenu multimédia tel que de la musique, des animations et des vidéos. La figure ci-dessus montre les icônes d'application sur l'écran d'accueil (à gauche), la lecture de musique (au centre) et l'affichage des widgets d'application (à droite). En haut de l'écran, une barre d'état affiche des informations sur le périphérique et sa connectivité. L'écran d'accueil Android peut être composé de plusieurs volets, et l'utilisateur glisse dans les deux sens.

Android est conçu pour fournir une réponse immédiate à la saisie de l'utilisateur. Outre une interface dynamique qui répond immédiatement au toucher, un appareil sous Android peut vibrer pour fournir un retour haptique. De nombreuses applications tirent parti du matériel interne tel que les accéléromètres, les gyroscopes et les capteurs de proximité pour répondre aux actions supplémentaires des utilisateurs. Ces capteurs peuvent également détecter la rotation de l'écran. Par exemple, vous pouvez concevoir un jeu de course dans lequel l'utilisateur fait pivoter l'appareil comme s'il s'agissait d'un volant.

La plate-forme Android, basée sur le [noyau Linux](https://en.wikipedia.org/wiki/Linux_kernel), est principalement conçue pour les appareils mobiles à écran tactile tels que les téléphones mobiles et les tablettes. Comme les appareils fonctionnant sous Android sont généralement alimentés par batterie, Android est conçu pour gérer les processus de manière à limiter la consommation d'énergie au minimum, permettant ainsi une utilisation plus longue de la batterie.

### Il est facile de développer des applications

Pour développer des applications qui tirent parti du système d'exploitation et de l'interface utilisateur Android, utilisez le kit de développement de logiciel Android (SDK). Le SDK comprend des bibliothèques de logiciels contenant du code prédéfini, un débogueur, un émulateur de périphérique, de la documentation, des exemples de code et des didacticiels. Utilisez le SDK pour créer des applications qui ont fière allure et tirez parti des capacités matérielles disponibles sur chaque appareil Android.

Pour développer des applications à l'aide du SDK, utilisez le [langage de programmation Java](https://en.wikipedia.org/wiki/Java_ (langage_programmation)) pour développer l'application et le [Langage de balisage extensible](https: // en. wikipedia.org/wiki/XML) (XML) pour décrire les ressources de données. En écrivant le code en Java et en créant un binaire d'application unique, vous créez une application pouvant s'exécuter à la fois sur les facteurs de forme des téléphones et des tablettes. Vous pouvez déclarer votre interface utilisateur dans des ensembles légers de ressources XML. Par exemple, créez un ensemble pour les parties de l'interface utilisateur communes à tous les facteurs de forme, et d'autres ensembles pour les fonctionnalités propres aux téléphones ou aux tablettes. Au moment de l'exécution, Android applique les ensembles de ressources appropriés en fonction de la taille de l'écran, de la densité de l'écran, des paramètres régionaux, etc. du périphérique.

Pour vous aider à développer efficacement vos applications, Google propose un environnement de développement intégré (IDE) appelé [Android Studio](https://developer.android.com/studio/index.html). Il offre des fonctionnalités avancées pour le développement, le débogage et le packaging d'applications Android. À l'aide d'Android Studio, vous pouvez développer pour tout appareil sous Android, ou créer des appareils virtuels qui émulent toute configuration matérielle.

Android fournit une architecture de développement riche. Vous n'avez pas besoin d'en savoir beaucoup sur les composants de cette architecture, mais il est utile de savoir ce qui est disponible dans le système pour votre application. Le diagramme ci-dessous présente les principaux composants de l’Android _stack_, à savoir le système d’exploitation et l’architecture de développement. ![La pile Android](images/dg_android_stack.png "La pile Android")

Dans la figure ci-dessus:

1. **_Apps:_** Vos applications vivent à ce niveau, ainsi que les applications système essentielles pour la messagerie électronique, la messagerie SMS, les calendriers, la navigation Internet et les contacts.
2. **_Infrastructure API Java:_** Toutes les fonctionnalités de développement Android, telles que [Composants d'interface utilisateur](https://developer.android.com/guide/topics/ui/overview.html), [Gestion des ressources](https: // developer.android.com/guide/topics/resources/overview.html) et [gestion du cycle de vie](https://developer.android.com/guide/components/activities.html) sont disponibles via des interfaces de programmation d'applications (API ). Vous n'avez pas besoin de connaître les détails du fonctionnement des API. Vous devez seulement apprendre à les utiliser.
3. **_Bibliothèques et environnement d'exécution Android:_** Chaque application s'exécute dans son propre processus, avec sa propre instance de l'environnement d'exécution Android. Android comprend un ensemble de bibliothèques d'exécution principales qui fournissent la plupart des fonctionnalités du langage de programmation Java. De nombreux composants et services système Android principaux sont construits à partir de code natif nécessitant des bibliothèques natives écrites en C et C ++. Ces bibliothèques natives sont disponibles pour les applications via la structure API Java.
4. **_Couche d'abstraction matérielle (HAL):_** Cette couche fournit des interfaces standard qui exposent les capacités matérielles des périphériques à la structure API Java supérieure. La couche HAL se compose de plusieurs modules de bibliothèque, chacun implémentant une interface pour un type spécifique de composant matériel, tel que la caméra ou le module Bluetooth.
5. **_Noyau Linux:_** Le noyau Linux est la base de la plate-forme Android. Les couches situées au-dessus du noyau Linux s’appuient sur le noyau Linux pour les threads, la gestion de la mémoire de bas niveau et d’autres fonctionnalités sous-jacentes. L'utilisation d'un noyau Linux permet à Android de tirer parti des fonctionnalités de sécurité basées sur Linux et aux fabricants de périphériques de développer des pilotes matériels pour un noyau bien connu.

### Nombreuses options de distribution

Vous pouvez distribuer votre application Android de différentes manières: par courrier électronique, sur un site Web ou sur un marché d'applications tel que [Google Play](https://play.google.com/store). Les utilisateurs d'Android téléchargent chaque mois des milliards d'applications et de jeux sur le Google Play Store. Google Play est un service de distribution numérique, exploité et développé par Google, qui sert de boutique d'applications officielle pour Android. Google Play permet aux consommateurs de parcourir et de télécharger des applications développées avec le SDK Android. ![Google Play sur un téléphone mobile Android](images/pv_gp-device.png)


### versions Android

Google fournit d'importantes mises à niveau incrémentielles du système d'exploitation Android à l'aide de noms sur le thème de la confiserie. La dernière version majeure est Android 8.0 "Oreo".


|||||
|--- |--- |--- |--- |
|**Code name**|**Version number**|**Initial release date**|**API level**|
|N/A|1.0|23 Septembre 2008|1|
|1.1|9 Février 2009|2|?|
|[Cupcake](https://en.wikipedia.org/wiki/Android_Cupcake) ![](../images/cupcake.png)|1.5|27 Avril 2009|3|
|[Donut](https://en.wikipedia.org/wiki/Android_Donut) ![](../images/donut_circle.png)|1.6|15 Septembre 2009|4|
|[Eclair](https://en.wikipedia.org/wiki/Android_Eclair) ![](../images/eclair_circle.png)|2.0 – 2.1|26 Octobre 2009|5–7|
|[Froyo](https://en.wikipedia.org/wiki/Android_Froyo) ![](../images/froyo_circle.png)|2.2 – 2.2.3|20 Mai 2010|8|
|[Gingerbread](https://en.wikipedia.org/wiki/Android_Gingerbread) ![](../images/gingerbread_circle.png)|2.3 – 2.3.7|6 Décembre 2010|9–10|
|[Honeycomb](https://en.wikipedia.org/wiki/Android_Honeycomb) ![](../images/honeycomb_circle.png)|3.0 – 3.2.6|22 Février 2011|11–13|
|[Ice Cream Sandwich](https://en.wikipedia.org/wiki/Android_Ice_Cream_Sandwich) ![](../images/icecream_circle.png)|4.0 – 4.0.4|18 Octobre 2011|14–15|
|[Jelly Bean](https://developer.android.com/about/versions/jelly-bean.html) ![](../images/jellybean_circle.png)|4.1 – 4.3.1|9 Juillet 2012|16–18|
|[KitKat](https://developer.android.com/about/versions/kitkat.html) ![](../images/kitkat_circle.png)|4.4 – 4.4.4|31 Octobre 2013|19–20|
|[Lollipop](https://developer.android.com/about/versions/lollipop.html) ![](../images/lollipop_circle.png)|5.0 – 5.1.1|12 Novembre 2014|21–22|
|[Marshmallow](https://developer.android.com/about/versions/marshmallow/index.html) ![](../images/marshmallow_circle.png)|6.0 – 6.0.1|5 Octobre 2015|23|
|[Nougat](https://developer.android.com/about/versions/nougat/index.html) ![](../images/nougat.png)|7.0|22 août 2016|24-25|
|[Oreo](https://developer.android.com/about/versions/oreo/) ![](../images/oreo_circle.png)|8.0|21 août 2017|26-27|
|[Pie](https://developer.android.com/about/versions/pie/) ![](images/pie_circle.png)|9.0|6 août 2018|28|

> Positive
> : consultez les versions précédentes et leurs fonctionnalités sur [L'histoire d'Android](https://www.android.com/history). Le [tableau de bord pour les versions de plate-forme](http://developer.android.com/about/dashboards/index.html) indique la répartition des périphériques actifs exécutant chaque version d'Android, en fonction du nombre de périphériques qui visitent le magasin Google Play. . Il est recommandé de prendre en charge environ 90% des appareils actifs, tout en ciblant votre application vers la dernière version.

**Remarque:**Pour fournir les meilleures fonctionnalités parmi les versions Android, utilisez [Android Support Library](https://developer.android.com/tools/support-library/index.html) dans votre application. Cette bibliothèque permet à votre application d'utiliser les dernières API de la plate-forme Android sur des appareils plus anciens. </ Div>

### Les défis du développement d'applications Android

Bien que la plate-forme Android offre de nombreuses fonctionnalités pour le développement d'applications, vous devez toutefois relever un certain nombre de défis, tels que:

* Construire pour un monde multi-écrans
* Obtenir de bonnes performances
* Garder votre code et vos utilisateurs plus sécurisés
* S'assurer que votre application est compatible avec les anciennes versions de la plateforme
* Comprendre le marché et l'utilisateur

### Construire pour un monde multi-écrans

Android fonctionne sur des milliards d'appareils de poche dans le monde et prend en charge divers facteurs de forme, notamment les appareils portables et les téléviseurs. Les appareils sont de différentes tailles et formes, ce qui a une incidence sur la conception des écrans et des éléments d'interface utilisateur de vos applications. ![Écrans de téléphones mobiles et tablettes](images/dg_phone_and_tablet.png "Écrans de téléphones mobiles et tablettes")

En outre, les fabricants de périphériques peuvent ajouter leurs propres éléments d'interface utilisateur, styles et couleurs pour différencier leurs produits. Chaque fabricant offre des fonctionnalités différentes en ce qui concerne les formes du clavier, la taille de l'écran ou les boutons de l'appareil photo. Une application qui s'exécute sur un appareil peut sembler légèrement différente sur un autre. En tant que développeur, votre défi consiste à concevoir des éléments d'interface utilisateur fonctionnant sur tous les appareils.

### Maximiser les performances de l'application

Les performances d'une application sont déterminées par sa vitesse d'exécution, sa facilité de connexion au réseau et sa capacité à gérer l'utilisation de la batterie et de la mémoire. Les performances sont affectées par des facteurs tels que la durée de vie de la batterie, le contenu multimédia et l'accès à Internet. Sachez que certaines fonctionnalités que vous concevez pour votre application peuvent entraîner des problèmes de performances pour les utilisateurs. Par exemple, pour économiser la batterie de l'utilisateur, activez les services d'arrière-plan uniquement lorsqu'ils sont nécessaires.

### Sécuriser votre code et vos utilisateurs

Vous devez prendre des précautions pour rendre votre code et l'expérience de l'utilisateur lors de l'utilisation de votre application aussi sécurisés que possible.

* Utilisez des outils tels que ProGuard, fourni dans Android Studio. ProGuard détecte et supprime les classes, champs, méthodes et attributs inutilisés.
* Cryptez l'intégralité du code et des ressources de votre application lors de son conditionnement.
* Pour protéger les informations critiques des utilisateurs, telles que les identifiants et les mots de passe, sécurisez votre canal de communication afin de protéger les données en transit sur Internet, ainsi que les données inactives sur l'appareil.

### Rester compatible avec les anciennes versions d'Android

La plate-forme Android continue de s'améliorer et offre de nouvelles fonctionnalités que vous pouvez ajouter à vos applications. Cependant, vous devez vous assurer que votre application peut toujours fonctionner sur des appareils dotés d'anciennes versions d'Android. Il n'est pas pratique de se concentrer uniquement sur la version Android la plus récente, car tous les utilisateurs ne peuvent pas avoir mis à niveau ou ne peuvent pas mettre à niveau leurs appareils. Heureusement, Android Studio offre aux développeurs des options leur permettant de rester plus facilement compatibles avec les anciennes versions.


### En savoir plus

Documentation de développement pour les développeurs Android:

*   [Developer Guides](https://developer.android.com/guide/index.html)
*   [Platform Architecture](https://developer.android.com/guide/platform/index.html)
*   [Layouts](https://developer.android.com/guide/topics/ui/overview.html)
*   [Supporting different platform versions](https://developer.android.com/training/basics/supporting-devices/platforms.html)

autres:

*   [Distribution dashboard](http://developer.android.com/about/dashboards/index.html)
*   [Meet Android Studio](https://developer.android.com/studio/intro/index.html)
*   Wikipedia: [Android version history](https://en.wikipedia.org/wiki/Android_version_history)



## Android Studio : Installation

Android Studio fournit un environnement de développement intégré complet comprenant un éditeur de code avancé et un ensemble de modèles d'application. En outre, il contient des outils de développement, de débogage, de test et de performance qui facilitent le développement d'applications. Vous pouvez tester vos applications avec une large gamme d'émulateurs préconfigurés ou sur votre propre appareil mobile, créer des applications de production et les publier sur le magasin Google Play.

**Remarque**: Android Studio est en constante amélioration. Pour obtenir les dernières informations sur la configuration système requise et les instructions d'installation, voir [Android Studio](https://developer.android.com/studio/index.html).

Android Studio est disponible pour les ordinateurs fonctionnant sous Windows ou Linux et pour les Mac exécutant macOS. Le plus récent OpenJDK (Java Development Kit) est fourni avec Android Studio.

Pour vous familiariser avec Android Studio, vérifiez d’abord la [configuration système requise](https://developer.android.com/studio/index.html#Requirements) pour vous assurer que votre système les respecte. L'installation est similaire pour toutes les plateformes. Toutes les différences sont notées ci-dessous.

1. Accédez au [site pour les développeurs Android](https://developer.android.com/sdk/index.html) et suivez les instructions pour télécharger et installer [installer Android Studio](https://developer.android.com/studio/install.html) :**https://developer.android.com/studio/install.html**.
2. Acceptez les configurations par défaut pour toutes les étapes et assurez-vous que tous les composants sont sélectionnés pour l'installation.
3. Une fois l'installation terminée, l'assistant d'installation télécharge et installe des composants supplémentaires, notamment le SDK Android. Soyez patient, cela peut prendre un certain temps en fonction de votre débit Internet, et certaines étapes peuvent sembler redondantes.
4. Une fois le téléchargement terminé, Android Studio démarre et vous êtes prêt à créer votre premier projet.

## Première Application Android

**Contenu:**

* [Le processus de développement](#développement)
* [Utiliser Android Studio](#android)
* [Exploration d'un projet](#exploration)
* [Comprendre le manifeste Android](#manifeste)
* [Comprendre le processus de construction](#build_configuration)
* [Exécuter l'application sur un émulateur ou un périphérique](#testing)
* [Utilisation du journal](#journal)
* [En savoir plus](#learnmore)


Ce chapitre explique comment développer des applications à l'aide d'Android Studio, qui est un environnement de développement intégré (IDE) pour Android.

### Le processus de développement

Un projet d'application Android commence par une idée et une définition des exigences nécessaires à la réalisation de cette idée. Vous voudrez peut-être esquisser des interfaces utilisateur pour les différentes fonctions de l'application. Pour montrer à quoi ressemblerait une interface utilisateur et son fonctionnement, utilisez des dessins, des maquettes et des prototypes.

Lorsque vous êtes prêt à commencer à coder, vous utilisez Android Studio pour exécuter les étapes suivantes:
![Processus de développement Android Studio](images/development_process_with_as.png)

1. Créez le projet dans Android Studio et choisissez un modèle approprié.
2. Définissez une mise en page pour chaque écran comportant des éléments d'interface utilisateur. Vous pouvez placer des éléments d'interface utilisateur à l'écran à l'aide de l'éditeur de disposition ou écrire du code directement dans le langage XML (Extensible Markup Language).
3. Écrivez du code en utilisant le langage de programmation Java. Créez du code source pour tous les composants de l'application.
4. Générez et exécutez l'application sur des appareils réels et virtuels. Utilisez la configuration de construction par défaut ou créez des versions personnalisées pour différentes versions de votre application. ©
5. Testez et déboguez la logique et l'interface utilisateur de l'application.
6. Publiez l'application en assemblant l'APK final (fichier de package) et en le distribuant via des canaux tels que Google Play.


### Utiliser Android Studio

Android Studio fournit un environnement de développement unifié permettant de créer des applications pour tous les appareils Android. Android Studio inclut des modèles de code avec un exemple de code pour les fonctionnalités communes de l'application, des outils de test et des frameworks complets, ainsi qu'un système de construction flexible.

### Démarrer un projet Android Studio

Une fois que vous avez correctement installé Android IDE, double-cliquez sur l’icône de l’application Android Studio pour le démarrer. Cliquez sur **Démarrer un nouveau projet Android Studio** dans la fenêtre de bienvenue et nommez le projet avec le même nom que vous souhaitez utiliser pour l'application. ![Création d'un projet Android](images/as_new_app1.png)

Lorsque vous choisissez un **domaine d'entreprise unique** , n'oubliez pas que les applications publiées sur Google Play doivent avoir un nom de package unique. Étant donné que les domaines sont uniques, le nom de l’application doit être précédé du nom de l’application. Si vous ne prévoyez pas de publier l'application, vous pouvez accepter le domaine d'exemple par défaut. Sachez que changer le nom du paquet plus tard est un travail supplémentaire.

### Choix des périphériques cibles et du SDK minimum

Lorsque vous choisissez des appareils Android cibles, **Téléphone et tablette** sont sélectionnés par défaut, comme indiqué dans la figure ci-dessous. Le choix indiqué dans la figure pour le SDK minimum - **API 15: Android 4.0.3 (IceCreamSandwich)** - rend votre application compatible avec 97% des appareils Android activés sur le Google Play Store.

![Sélection des appareils Android ciblés pour l'application](images/as_new_app2.png)

Différents appareils exécutent différentes versions du système Android, telles que Android 4.0.3 ou Android 4.4 \. Chaque version successive ajoute souvent de nouvelles API non disponibles dans la version précédente. Pour indiquer quel jeu d'API est disponible, chaque version spécifie un niveau d'API. Par exemple, Android 1.0 correspond au niveau 1 de l'API et Android 4.0.3 au niveau 15 de l'API \.

Le SDK minimum déclare la version Android minimale pour votre application. Chaque version successive d'Android assure la compatibilité des applications construites à l'aide des API des versions précédentes. Cela signifie que votre application doit toujours être compatible avec les futures versions d'Android, si vous utilisez les API documentées d'Android.

### Choisir un modèle d'activité

Un [Activity](https://developer.android.com/reference/android/app/Activity.html) est une tâche unique et ciblée que l'utilisateur peut effectuer. C'est un élément crucial de toute application Android. Une mise en page est généralement associée à une mise en page qui définit la manière dont les éléments de l'interface utilisateur apparaissent sur un écran.

Android Studio pré-remplit votre projet avec un code minimal pour une `Activity` et une mise en page basée sur un _template_. Les modèles de `Activity` disponibles vont d'un modèle pratiquement vierge (**Ajouter aucune activité**) à une` Activité` comprenant une navigation et un menu d'options.

![Sélectionnez le modèle d'activité vide](images/as_new_app3_empty_activity.png)

Vous pouvez personnaliser la `Activité` après avoir sélectionné votre modèle. Par exemple, l'option**Activité vide**fournit une seule `Activité` avec une seule ressource de présentation pour l'écran. L'écran**Configurer l'activité**apparaît après que vous ayez cliqué sur**Suivant**. Sur l'écran**Configurer l'activité**, vous pouvez accepter le nom couramment utilisé pour `Activity` (tel que` MainActivity`) ou vous pouvez le modifier.

> Positive
> : Ce cours couvre la classe `Activité` plus en détail dans une autre pratique. Vous pouvez également lire [Introduction aux activités](https://developer.android.com/guide/components/activities/intro-activities.html) pour une introduction complète.

![Configuration de l'activité](images/as_new_app4_layout_file.png)

L'écran**Configurer l'activité**diffère selon le modèle que vous avez choisi. Dans la plupart des cas, vous pouvez sélectionner les options suivantes, si elles ne le sont pas déjà:

***Générer un fichier de mise en page**: laissez cette case cochée pour créer la ressource de mise en page connectée à cette `Activity`, généralement nommée` activity_main`. La mise en page définit l'interface utilisateur de l'activité.
***Compatibilité descendante (AppCompat):**Laissez cette case cochée pour inclure la bibliothèque `AppCompat`. Utilisez la bibliothèque `AppCompat` pour vous assurer que l'application est compatible avec les versions précédentes d'Android, même si l'application utilise des fonctionnalités trouvées uniquement dans les versions plus récentes d'Android.

Android Studio crée un dossier pour vos projets et construit le projet avec [Gradle](https://gradle.org/).

> Positive
> : Consultez la page de développeur [Configure your build](https://developer.android.com/studio/build/index.html) pour obtenir des informations détaillées.


### Explorer un projet

Un projet Android Studio contient tout le code source et toutes les ressources d'une application. Les ressources comprennent des mises en page, des chaînes, des couleurs, des dimensions et des images. La fenêtre principale d'Android Studio est composée de plusieurs zones logiques, ou _panes_, comme indiqué dans la figure ci-dessous.

![Volets de projet Android Studio](images/as_gradle_in_project_pane_annot.png)

Dans la figure ci-dessus:

1. Barre d'outils: fournit un large éventail d'actions, notamment l'exécution de l'application Android et le lancement d'outils Android.
2. Barre de navigation: naviguez dans le projet et ouvrez les fichiers pour les éditer.
3. Volet**Projet**: affiche les fichiers de projet dans une hiérarchie. La hiérarchie sélectionnée dans la figure ci-dessus est**Android**.
4. Editeur: Le contenu d'un fichier sélectionné dans le projet. Par exemple, après avoir sélectionné une mise en page (comme illustré dans la figure ci-dessus), le volet de l'éditeur affiche l'éditeur de mise en page avec des outils pour modifier la mise en page. Une fois que vous avez sélectionné un fichier de code Java, le volet de l'éditeur affiche le code Java avec des outils pour l'éditer.
5. Onglets situés à gauche, à droite et en bas de la fenêtre: vous pouvez cliquer sur des onglets pour ouvrir d'autres volets, tels que**Logcat**, pour ouvrir le volet**Logcat**avec les messages du journal ou**TODO**. gérer des tâches.

La barre d'état située au bas de la fenêtre d'Android Studio affiche l'état du projet et d'Android Studio lui-même, ainsi que les avertissements et les messages éventuels. Vous pouvez voir la progression de la construction dans la barre d'état.

> Positive
> : Vous pouvez organiser la fenêtre principale pour vous donner plus d’espace à l’écran en masquant ou en déplaçant les volets. Vous pouvez également utiliser des raccourcis clavier pour accéder à la plupart des fonctionnalités.

Voir [Raccourcis clavier](https://developer.android.com/studio/intro/keyboard-shortcuts.html) pour une liste complète.

### Utilisation de la fenêtre de projet

Vous pouvez afficher l'organisation du projet de plusieurs manières dans la fenêtre Projet. S'il n'est pas déjà sélectionné, cliquez sur l'onglet**Projet**. (L'onglet**Projet**se trouve dans la colonne d'onglets verticale du côté gauche de la fenêtre d'Android Studio.)

La fenêtre de projet apparaît. Pour afficher le projet dans la hiérarchie de projets Android standard, sélectionnez**Android**à partir de la flèche vers le bas située en haut du volet**Projet**.

![Volet Projet>Android](images/as_project_android_menu.png)

**Remarque:**Ce chapitre et d'autres chapitres font référence à la sous-fenêtre Projet, lorsqu'elle est définie sur**Android**, sous le volet**Projet>Android**.


#### Gradle files

Lorsque vous créez un projet pour la première fois, le volet**Projet>Android**apparaît avec le dossier `Gradle Scripts` développé comme indiqué ci-dessous. Si le dossier `Gradle Scripts` n'est pas développé, cliquez sur le triangle pour le développer. Ce dossier contient tous les fichiers nécessaires au système de construction.

![Dossier Gradle Scripts](images/as_project_android_gradle_folder.png)

Le fichier `build.gradle (Module: app)` spécifie des bibliothèques supplémentaires et la configuration de construction du module. Le modèle `Activity` que vous sélectionnez crée ce fichier. Le fichier inclut l'attribut `minSdkVersion` qui déclare la version minimale de l'application et l'attribut` targetSdkVersion` qui déclare la version la plus récente (la plus récente) pour laquelle l'application a été optimisée.

Ce fichier contient également une liste de _dependencies_, bibliothèques requises par le code, telles que la bibliothèque `AppCompat` pour la prise en charge d'un large éventail de versions Android.

#### Code de l'application

Pour afficher et modifier le code Java, développez le dossier `app`, le dossier` java` et le dossier `com.example.android.helloworld`. Double-cliquez sur le fichier `MainActivity`` java` pour l'ouvrir dans l'éditeur de code.

![Le dossier de l'application](images/as_project_android_app_folder.png)

Le dossier `java` inclut les fichiers de classe Java. Chaque [Activité](https://developer.android.com/reference/android/app/Activity.html), [ Service](https://developer.android.com/reference/android/app/ Service.html) ou un autre composant (tel qu'un [Fragment]](https://developer.android.com/reference/android/app/Fragment.html)) est défini en tant que classe Java, généralement dans sa propre fichier. Les tests et autres fichiers de classe Java se trouvent également ici.


Le dossier `java` contient trois sous-dossiers:

* `com.example.hello.helloworld` (ou le nom de domaine que vous avez spécifié)**:**Tous les fichiers d'un package se trouvent dans un dossier nommé d'après le package. Pour votre application Hello World, il existe un package qui ne contient que `MainActivity.java`. La première `Activity` (écran) visible par l'utilisateur, qui initialise également les ressources à l'échelle de l'application, est généralement appelée` MainActivity`. (L'extension de fichier est omise dans le volet**Projet>Android**.)
* `com.example.hello.helloworld (androidTest)`: Ce dossier est destiné à vos tests instrumentés et commence avec un fichier de test squelette.
* `com.example.hello.helloworld (test)`: ce dossier est destiné à vos tests unitaires et commence avec un fichier de test unitaire créé automatiquement.


#### Fichiers de mise en page

Pour afficher et éditer un fichier de présentation, développez le dossier `res` et le dossier` layout` pour afficher le fichier de présentation. Dans la figure ci-dessous, le fichier de présentation s'appelle `activity_main.xml`.

Double-cliquez sur le fichier pour l'ouvrir dans l'éditeur de disposition. Les fichiers de mise en page sont écrits en XML.

![Le dossier res](images/as_project_android_res_folder.png)

#### Fichiers de ressources

Le dossier `res` contient des ressources, telles que des dispositions, des chaînes et des images. Une `Activité` est généralement associée à une disposition de vues d'interface utilisateur définies comme un fichier XML. Ce fichier XML est généralement nommé d'après son `Activity`. Le dossier `res` comprend ces sous-dossiers:

* `drawable`: Stockez toutes les images de votre application dans ce dossier.
* `layout`: chaque` Activity` a au moins un fichier de disposition XML qui décrit l'interface utilisateur. Pour Hello World, ce dossier contient `activity_main.xml`.
* `mipmap`: Les icônes du lanceur sont stockées dans ce dossier. Il existe un sous-dossier pour chaque densité d'écran prise en charge. Android utilise la densité de l'écran (le nombre de pixels par pouce) pour déterminer la résolution de l'image requise. Android regroupe toutes les densités d'écran réelles en densités généralisées, telles que moyenne (mdpi), élevée (hdpi) ou extra-extra-extra-haute (xxxhdpi). Le dossier `ic_launcher.png` contient les icônes de lanceur par défaut pour toutes les densités prises en charge par votre application.
* `values`: au lieu de coder en dur des valeurs telles que des chaînes, des dimensions et des couleurs dans vos fichiers XML et Java, il est recommandé de les définir dans leurs fichiers` valeurs` respectifs. Cette pratique facilite la modification des valeurs et leur cohérence dans l'ensemble de votre application.

Le sous-dossier `values` inclut ces sous-dossiers:

* `colors.xml`: Affiche les couleurs par défaut pour le thème choisi. Vous pouvez ajouter vos propres couleurs ou modifier les couleurs en fonction des besoins de votre application.
* `dimens.xml`: Stocke les tailles des vues et des objets pour différentes résolutions.
* `strings.xml`: Créez des ressources pour toutes vos chaînes. Cela facilite la traduction des chaînes dans d'autres langues.
* `styles.xml`**:**Tous les styles de votre application et de votre thème sont affichés ici. Les styles aident à donner à votre application un aspect cohérent pour tous les éléments de l'interface utilisateur.


### Utilisation du volet de l'éditeur

Si vous sélectionnez un fichier, le volet de l'éditeur apparaît. Un onglet apparaît pour le fichier afin que vous puissiez ouvrir plusieurs fichiers et basculer entre eux. Par exemple, si vous double-cliquez sur le fichier de mise en forme**activity_main.xml**dans le volet**Projet>Android**, l'éditeur de mise en page apparaît, comme illustré ci-dessous.

![L'éditeur de disposition](images/as_activity_layout_tab.png)

Si vous double-cliquez sur le fichier**MainActivity**dans le volet**Projet>Android**, l'éditeur passe à l'éditeur de code comme indiqué ci-dessous, avec un onglet pour**MainActivity.java**:

![Le code éditeur](images/as_mainactivity_tab.png)

En haut du fichier `MainActivity.java` se trouve une instruction` package` qui définit le package de l'application. Cette instruction de paquet est suivie d'un bloc `import` condensé avec` ... `, comme le montre la figure ci-dessus. Cliquez sur les points pour développer le bloc et l'afficher. Les instructions `import` importent les bibliothèques nécessaires à l'application. Par exemple, l'instruction suivante importe la bibliothèque `AppCompatActivity`:

    import android.support.v7.app.AppCompatActivity;

Chaque `Activity` dans une application est implémentée en tant que classe Java. La déclaration de classe suivante étend la classe `AppCompatActivity` pour implémenter les fonctionnalités d'une manière compatible avec les versions précédentes d'Android:

    Classe publique MainActivity étend AppCompatActivity {
        // ... Reste du code pour la classe.
    }


### Comprendre le manifeste Android

Avant que le système Android puisse démarrer un composant d'application tel qu'une `Activité`, le système doit savoir que cette activité existe. Pour ce faire, lisez le fichier `AndroidManifest.xml` de l'application, qui décrit tous les composants de votre application Android. Chaque `Activité` doit figurer dans ce fichier XML, ainsi que tous les composants de l'application.

Pour afficher et modifier le fichier `AndroidManifest.xml`, développez le dossier` manifestes` dans le volet**Projet>Android**, puis double-cliquez sur `AndroidManifest.xml`. Son contenu apparaît dans le volet d'édition:

        <? xml version = "1.0" encoding = "utf-8"?>
        <manifest xmlns: android = "http://schemas.android.com/apk/res/android"
            package = "com.example.android.helloworld">
            <application
                android: allowBackup = "true"
                android: icon = "@ mipmap/ic_launcher"
                android: label = "@ string/nom_app"
                android: roundIcon = "@ mipmap/ic_launcher_round"
                android: supportsRtl = "true"
                android: theme = "@ style/AppTheme">
                <activité android: name = ". MainActivity">
                    <filtre d'intention>
                       <action android: name = "android.intent.action.MAIN" />
                       <category android: name = "android.intent.category.LAUNCHER" />
                    </ intent-filter>
                </ activity>
            </ application>
        </ manifest>
  

### Espace de noms Android et balise d'application

Le manifeste Android est codé en XML et utilise toujours le namespace Android:

    xmlns: android = "http://schemas.android.com/apk/res/android"
       package = "com.example.android.helloworld">

L'expression `package` indique le nom unique du package de la nouvelle application. Ne modifiez pas l'expression du package après la publication de l'application.

La balise `<application>`, avec sa balise de fermeture `</ application>`, définit les paramètres du manifeste pour l'ensemble de l'application.

### Sauvegarde automatique

L'attribut `Android: allowBackup` permet la sauvegarde automatique des données d'application:

    android: allowBackup = "true"

Définir l'attribut `android: allowBackup` sur` true` permet à l'application d'être sauvegardée automatiquement et restaurée au besoin. Les utilisateurs investissent temps et efforts pour configurer leurs applications. Le passage à un nouvel appareil peut annuler toute cette configuration soignée. Le système effectue cette sauvegarde automatique pour presque toutes les données d'application par défaut, sans que le développeur ait à écrire de code d'application supplémentaire.

Pour les applications dont la version du kit de développement cible est Android 6.0 (niveau 23) et supérieur, les appareils exécutant Android 6.0 et supérieur créent automatiquement des sauvegardes des données de l'application sur le cloud, car l'attribut `android: allowBackup` est défini par défaut sur` true` s'il est omis. Pour les applications niveau API 22, vous devez explicitement ajouter l'attribut `Android: allowBackup` et le définir sur` true`.

> Positive
> : Pour en savoir plus sur la sauvegarde automatique des applications, voir [Configuration de la sauvegarde automatique des applications](https://developer.android.com/training/backup/autosyncapi.html).



### L'icône de l'application

L'attribut `android: icon` définit l'icône de l'application:

    android: allowBackup = "true"
    android: icon = "@ mipmap/ic_launcher"

L'attribut `android: icon` attribue à l'application une icône dans le dossier` mipmap` (à l'intérieur du dossier `res` dans le volet**Projet>Android**). L'icône apparaît sur l'écran d'accueil ou dans l'écran Rechercher des applications pour lancer l'application. L'icône sert également d'icône par défaut pour les composants de l'application.

![L'icône du lanceur standard d'un nouveau projet apparaît dans l'écran Rechercher des applications.](images/pv_launcher_icon1.png)

### Étiquette d'application et ressources de chaîne

L'attribut `android: label` affiche la chaîne` "Hello World" `en surbrillance. Si vous cliquez sur la chaîne, l'affichage de la ressource `@ string/nom_app 'est modifié:


        android: label = "@ string/nom_app"

    

> Positive
Pour voir le menu contextuel, ctrl-cliquez ou cliquez-droit sur `app_name` dans le volet de l'éditeur. Sélectionnez**Aller à>Déclaration**pour voir où la ressource chaîne est déclarée: dans le fichier `strings.xml`. Lorsque vous sélectionnez**Aller à>Déclaration**ou ouvrez le fichier en double-cliquant sur `strings.xml` dans le dossier` values` dans le volet**Projet>Android**, le contenu du fichier apparaît dans le volet d'édition.

Après avoir ouvert le fichier `strings.xml`, vous pouvez constater que le nom de chaîne` app_name` est défini sur `Hello World`. Vous pouvez modifier le nom de l'application en modifiant la chaîne `Hello World`. Les ressources de chaîne sont décrites dans une leçon séparée.

Thème de l'application

L'attribut `android: theme` définit le thème de l'application, qui définit l'apparence des éléments de l'interface utilisateur tels que le texte:

    android: theme = "@ style/AppTheme"

L'attribut `theme` est défini sur le thème standard` AppTheme`. Les thèmes sont décrits dans une leçon séparée.


### Déclarer la version Android

Différents périphériques peuvent exécuter différentes versions du système Android, telles que Android 4.0 ou Android 4.4 \. Chaque version successive peut ajouter de nouvelles API non disponibles dans la version précédente. Pour indiquer quel jeu d'API est disponible, chaque version spécifie un niveau d'API. Par exemple, Android 1.0 correspond au niveau 1 de l'API et Android 4.4 au niveau 19 de l'API.


Le niveau de l'API permet au développeur de déclarer la version minimale avec laquelle l'application est compatible, à l'aide de la balise `<uses-sdk>` du manifeste et de son attribut `minSdkVersion`. Par exemple, les API du fournisseur de calendrier ont été ajoutées dans Android 4.0 (API de niveau 14). Si votre application ne peut pas fonctionner sans ces API, déclarez le niveau 14 de l'API comme version minimale prise en charge de l'application, comme suit:

    <manifest xmlns:android="http://schemas.android.com/apk/res/android"
        package="com.example.android.helloworld">
        <uses-sdk android:minSdkVersion="14" android:targetSdkVersion="19" />
        // ... Rest of manifest information
    </manifest>

L'attribut `minSdkVersion` déclare la version minimale de l'application et l'attribut` targetSdkVersion` déclare la version la plus récente (la plus récente) optimisée au sein de l'application. Chaque version successive d'Android assure la compatibilité des applications créées à l'aide des API des versions précédentes. L'application doit donc toujours être compatible avec les versions futures d'Android tout en utilisant les API documentées d'Android.

L'attribut `targetSdkVersion` n'empêche pas l'installation d'une application sur les versions d'Android supérieures (plus récentes) à la valeur spécifiée. Même dans ce cas, l'attribut cible est important car il indique au système si l'application doit hériter des changements de comportement dans les versions les plus récentes.

Si vous ne mettez pas à jour le `targetSdkVersion` vers la dernière version, le système suppose que votre application nécessite des comportements rétrocompatibles lorsqu'elle s'exécute sur la dernière version. Par exemple, parmi les changements de comportement dans Android 4.4, les alarmes créées avec les API `AlarmManager` sont maintenant inexactes par défaut, de sorte que le système peut traiter les alarmes d'application par lots et préserver son alimentation. Si votre niveau d'API cible est inférieur à «19», le système conserve le comportement de l'API précédente pour votre application.


### Comprendre le processus de construction

Le package d'application Android (APK) est le format de fichier de package permettant de distribuer et d'installer des applications mobiles Android. Le processus de construction implique des outils et des processus qui convertissent automatiquement chaque projet en un APK.

Android Studio utilise Gradle comme base du système de construction, avec des fonctionnalités plus spécifiques à Android fournies par le plug-in Android pour Gradle. Ce système de compilation s’exécute en tant qu’outil intégré à partir du menu Android Studio.

### Comprendre les fichiers build.gradle

Lorsque vous créez un projet, Android Studio génère automatiquement les fichiers de construction nécessaires dans le dossier `Gradle Scripts` du volet**Projet>Android**. Les fichiers de construction d'Android Studio sont nommés `build.gradle`, comme indiqué ci-dessous:

![Scripts Gradle](images/as_project_android_gradle_folder.png)

### build.gradle (Project: _apptitle_)

Ce fichier est le fichier de construction de niveau supérieur pour l'ensemble du projet, situé dans le dossier du projet racine, qui définit les configurations de construction qui s'appliquent à tous les modules de votre projet. Ce fichier, généré par Android Studio, ne doit pas être modifié pour inclure les dépendances de l'application.

Si une dépendance est autre chose qu'une bibliothèque locale ou une arborescence de fichiers, Gradle recherche les fichiers dans les référentiels en ligne spécifiés dans le bloc référentiels de ce fichier. Par défaut, les nouveaux projets Android Studio déclarent que JCenter et Google (qui inclut le [référentiel Google Maven](https://maven.google.com/)] sont les emplacements du référentiel:

>``` bash
>    allprojects {
        repositories {
            google()
            jcenter()
        }
    }
>```


### build.gradle (module: app)

Android Studio crée des fichiers `build.gradle (Module: app)` distincts pour chaque module. Vous pouvez modifier les paramètres de génération pour fournir des options de personnalisation personnalisées pour chaque module, telles que des types de construction et des variantes de produit supplémentaires, ainsi que pour remplacer les paramètres du fichier manifeste ou du fichier build.gradle de niveau supérieur. Ce fichier est le plus souvent le fichier à modifier lors de la modification de configurations au niveau de l'application, telles que la déclaration de dépendances dans la section `dependencies`. Ce qui suit montre le contenu du fichier `build.gradle (Module: app)` d'un projet:


>``` bash
>   apply plugin: 'com.android.application'

    android {
        compileSdkVersion 26
        defaultConfig {
            applicationId "com.example.android.helloworld"
            minSdkVersion 15
            targetSdkVersion 26
            versionCode 1
            versionName "1.0"
            testInstrumentationRunner
                             "android.support.test.runner.AndroidJUnitRunner"
        }
        buildTypes {
            release {
                minifyEnabled false
                proguardFiles getDefaultProguardFile('proguard-android.txt'),
                                                         'proguard-rules.pro'
            }
        }
    }

    dependencies {
        implementation fileTree(dir: 'libs', include: ['*.jar'])
        implementation 'com.android.support:appcompat-v7:26.1.0'
        implementation 'com.android.support.constraint:constraint-layout:1.0.2'
        testImplementation 'junit:junit:4.12'
        androidTestImplementation 'com.android.support.test:runner:1.0.1'
        androidTestImplementation
                        'com.android.support.test.espresso:espresso-core:3.0.1'
    }
>``


Les fichiers `build.gradle` utilisent la syntaxe Gradle. Gradle est un langage DSL (Domain Specific Language) permettant de décrire et de manipuler la logique de construction à l'aide de [Groovy](http://groovy-lang.org/), langage dynamique pour la machine virtuelle Java (JVM). Vous n'avez pas besoin d'apprendre Groovy pour apporter des modifications, car le plug-in Android pour Gradle introduit la plupart des éléments DSL dont vous avez besoin.

> Positive
> : Pour en savoir plus sur le plugin Android DSL, lisez la [Documentation de référence DSL](http://google.github.io/android-gradle-dsl/current/index.html).

#### Plugin et blocs Android

Dans le fichier `build.gradle (Module: app)` ci-dessus, la première instruction applique les tâches de construction du plug-in Gradle spécifiques à Android:


    apply plugin: 'com.android.application'

    android {
       compileSdkVersion 26
       // ... Rest of android block.
    }

Le bloc `android {}` spécifie la version du SDK cible pour la compilation du code de l'application (`compileSdkVersion 26`) et de plusieurs blocs d'informations.

#### Le bloc defaultConfig

Les paramètres et entrées de base de l'application sont spécifiés dans le bloc `defaultConfig {}` du bloc `android {}:`

    defaultConfig {
        applicationId "com.example.android.helloworld"
        minSdkVersion 15
        targetSdkVersion 26
        versionCode 1
        versionName "1.0"
        testInstrumentationRunner
                    "android.support.test.runner.AndroidJUnitRunner"
    }

Les paramètres `minSdkVersion` et` targetSdkVersion` remplacent les paramètres `AndroidManifest.xml` pour la version minimale du SDK et la version du SDK cible. Reportez-vous à la section "Déclaration de la version Android" précédemment dans ce chapitre pour obtenir des informations générales sur ces paramètres.

L'instruction `testInstrumentationRunner` ajoute le support d'instrumentation pour tester l'interface utilisateur en utilisant Espresso et UIAutomator. Ces outils sont décrits dans une leçon séparée.

#### Types de construction

Les types de construction de l'application sont spécifiés dans un bloc `buildTypes {}`, qui contrôle la manière dont l'application est construite et empaquetée.

    buildTypes {
        release {
            minifyEnabled false
            proguardFiles getDefaultProguardFile('proguard-android.txt'),
                                                           'proguard-rules.pro'
        }
    }

Le type de construction spécifié est `release` pour la version de l'application. Un autre type de construction commun est `debug`. La configuration des types de construction est décrite dans une leçon séparée.

#### Dépendances

Les dépendances pour l'application sont définies dans le bloc `dependencies {}`, qui est la partie du fichier `build.gradle` qui est la plus susceptible de changer à mesure que vous commencez à développer du code qui dépend d'autres bibliothèques. Le bloc fait partie de l'API Gradle standard et appartient à _outside_ le bloc `android {}`.

    dependencies {
        implementation fileTree(dir: 'libs', include: ['*.jar'])
        implementation 'com.android.support:appcompat-v7:26.1.0'
        implementation 'com.android.support.constraint:constraint-layout:1.0.2'
        testImplementation 'junit:junit:4.12'
        androidTestImplementation 'com.android.support.test:runner:1.0.1'
        androidTestImplementation
                        'com.android.support.test.espresso:espresso-core:3.0.1'
    }

Dans l'extrait de code ci-dessus, l'instruction `implementation fileTree (dir: 'libs', include: ['* .jar'])` ajoute une dépendance de tous les fichiers ".jar" dans le dossier `libs`.

### Synchroniser votre projet

Lorsque vous apportez des modifications aux fichiers de configuration de la construction dans un projet, Android Studio nécessite que vous _sync_ les fichiers du projet. Lors de la synchronisation, Android Studio importe les modifications de configuration de génération et exécute des vérifications pour s'assurer que la configuration ne créera pas d'erreurs de construction.

Pour synchroniser les fichiers du projet, cliquez sur**Sync Now**dans la barre de notification qui apparaît lorsque vous effectuez une modification (comme illustré dans la figure ci-dessous) ou cliquez sur le bouton**Synchroniser le projet avec des fichiers Gradle**![Sync Project with Fichiers Gradle](images/ic_gradle_sync.png "Projet de synchronisation avec des fichiers Gradle") dans la barre de menus.

![Modification de la configuration de l'application Gradle](images/as_build_gradle_sync.png)

Si Android Studio constate des erreurs de configuration, par exemple, si le code source utilise des fonctionnalités d'API uniquement disponibles à un niveau d'API supérieur à `compileSdkVersion` - la fenêtre**Messages**semble décrire le problème.


### Exécuter l'application sur un émulateur ou un appareil

Avec les émulateurs de périphériques virtuels, vous pouvez tester une application sur différents périphériques, tels que des tablettes ou des smartphones, avec différents niveaux d'API pour différentes versions d'Android, afin de vous assurer qu'elle est correcte et qu'elle convient à la plupart des utilisateurs. Vous n'avez pas besoin de disposer d'un périphérique physique pour le développement d'applications.

Le [gestionnaire de périphériques virtuels Android](http://developer.android.com/tools/devices/managing-avds.html) crée un périphérique virtuel ou un émulateur qui simule la configuration d'un type particulier de périphérique Android. . Utilisez le gestionnaire AVD pour définir les caractéristiques matérielles d’un périphérique et son niveau d’API, puis pour l’enregistrer en tant que configuration de périphérique virtuel. Lorsque vous démarrez l'émulateur Android, celui-ci lit une configuration spécifiée et crée sur votre ordinateur un périphérique émulé qui se comporte exactement comme une version physique de ce périphérique.


### Création d'un périphérique virtuel

Pour exécuter un émulateur sur votre ordinateur, utilisez le gestionnaire AVD pour créer une configuration décrivant le périphérique virtuel. Sélectionnez**Outils>Android>Gestionnaire AVD**ou cliquez sur l'icône**Gestionnaire AVD**

![Icône Gestionnaire AVD](images/ic_avd_manager.png) dans la barre d’outils.

L'écran**Vos périphériques virtuels**apparaît, affichant tous les périphériques virtuels créés précédemment. Cliquez sur le bouton**+ Créer un périphérique virtuel**pour créer un nouveau périphérique virtuel. ![Gestionnaire de périphériques virtuels Android (images/as_avd_manager1.png "Gestionnaire de périphériques virtuels Android")

Vous pouvez sélectionner un périphérique dans une liste de périphériques matériels prédéfinis. Pour chaque périphérique, le tableau fournit une colonne pour sa taille d'affichage diagonale (**Taille**), sa résolution d'écran en pixels (**Résolution**) et sa densité de pixels (**Densité**). Par exemple, la densité de pixels du périphérique Nexus 5 est `xxhdpi`, ce qui signifie que l’application utilise les icônes du dossier` xxhdpi` du dossier `mipmap`. De même, l'application utilise des mises en page et des tirages à partir de dossiers définis pour cette densité.

![Sélection du périphérique matériel](images/as_avd_manager2.png)

Après avoir cliqué sur**Suivant**, l'écran**Image système**apparaît pour vous permettre de choisir la version du système Android pour le périphérique. L'onglet**Recommended**indique les systèmes recommandés pour le périphérique. D'autres versions sont disponibles sous les onglets**x86 Images**et**Autres images**. Si un lien**Télécharger**est visible à côté d'une version de l'image système, celle-ci n'est pas encore installée. Cliquez sur le lien pour lancer le téléchargement, puis cliquez sur**Terminer**lorsque vous avez terminé.

### Exécution de l'application sur le périphérique virtuel

Pour exécuter l'application sur le périphérique virtuel que vous avez créé dans la section précédente, procédez comme suit:

1. Dans Android Studio, sélectionnez**Exécuter>Exécuter l'application**ou cliquez sur l'icône ![Icône Android Studio Run](images/ic_run.png)**Icône Run**dans la barre d’outils.

2. Dans la fenêtre Sélectionner une cible de déploiement, sous Émulateurs disponibles, sélectionnez le périphérique virtuel que vous avez créé, puis cliquez sur**OK**.

L'émulateur démarre et démarre comme un périphérique physique. En fonction de la vitesse de votre ordinateur, le processus de démarrage peut prendre un certain temps. L’application est construite et, une fois l’émulateur prêt, Android Studio la télécharge sur l’émulateur et l’exécute.

L'application devrait être créée à partir du modèle d'activité vide ("Hello World"), comme indiqué dans la figure suivante, qui affiche également le volet**Exécuter**d'Android Studio qui affiche les actions effectuées pour exécuter l'application sur l'émulateur.

> Positive
> : lors des tests sur un périphérique virtuel, il est recommandé de le démarrer une fois, au tout début de votre session. Ne le fermez pas tant que vous n'avez pas terminé de tester votre application, afin que celle-ci ne subisse plus le processus de démarrage de l'appareil. Pour fermer le périphérique virtuel, sélectionnez**Quit**dans le menu ou appuyez sur**Control-Q**sous Windows ou**Command-Q**sous macOS.

![Emulateur et journal d'exécution](images/as_emulator_log_annotated.png)

La figure ci-dessus montre l'émulateur et le journal d'exécution:

1. L'émulateur exécutant l'application.
2. Le volet**Exécuter**, qui présente les actions entreprises pour installer et exécuter l'application.
3. L'onglet**Exécuter**sur lequel vous cliquez pour ouvrir ou fermer le volet**Exécuter**.


### Exécution de l'application sur un périphérique physique

Testez toujours vos applications sur un périphérique physique. Bien que les émulateurs soient utiles, ils ne peuvent pas afficher tous les états de périphérique possibles, tels que ce qui se passe si un appel entrant se produit pendant l'exécution de l'application. Pour exécuter l'application sur un périphérique physique, vous devez disposer des éléments suivants:

* Un appareil sous Android, tel qu'un téléphone ou une tablette.
* Un câble de données pour connecter votre appareil Android à votre ordinateur via le port USB.
* Si vous utilisez un système Linux ou Windows, vous devrez peut-être exécuter des étapes supplémentaires pour pouvoir fonctionner sur un périphérique matériel. Consultez la documentation [Utilisation de périphériques matériels](http://developer.android.com/tools/device.html). Vous devrez peut-être également installer le pilote USB approprié pour votre appareil. Voir [Pilotes USB OEM](http://developer.android.com/tools/extras/oem-usb.html).

Pour permettre à Android Studio de communiquer avec votre appareil Android, vous devez activer le débogage USB sur l'appareil. Vous activez le débogage USB dans les paramètres**Options du développeur**du périphérique. (Notez que l'activation du débogage USB n'est pas la même chose que l'enracinement de votre périphérique.)

Sur Android 4.2 et les versions ultérieures, l'écran**Options pour les développeurs**est masqué par défaut. Pour afficher les options du développeur et activer le débogage USB:

1. Sur votre appareil, ouvrez**Paramètres>À propos du téléphone**et appuyez sur**Numéro de construction**sept fois.
2. Revenez à l'écran précédent (**Paramètres**).**Options du développeur**apparaît en bas de la liste. Appuyez sur**Options du développeur**.
3. Sélectionnez**Débogage USB**.
4. Connectez l'appareil et lancez l'application depuis Android Studio.

### Utiliser le journal

Le journal est un puissant outil de débogage que vous pouvez utiliser pour examiner les valeurs, les chemins d’exécution et les exceptions. Une fois que vous avez ajouté des instructions de journalisation à une application, vos messages de journalisation apparaissent avec les messages de journalisation généraux dans le volet**Logcat**.

### Affichage des messages du journal

Pour afficher le volet**Logcat**, cliquez sur l'onglet**Logcat**au bas de la fenêtre d'Android Studio, comme indiqué dans la figure ci-dessous.

![Android Studio Logcat](images/as_window_logcat_annot.png)

Dans la figure ci-dessus:

1. L'onglet**Logcat**pour ouvrir et fermer le volet**Logcat**, qui affiche des informations sur votre application en cours d'exécution. Si vous ajoutez des instructions `Log` à votre application, les messages` Log` apparaissent ici.
2. Le menu `Log` level 'est réglé sur**Verbose**(valeur par défaut), qui affiche tous les messages` Log`. Les autres paramètres incluent**Debug**,**Error**,**Info**et**Warn**.


### Ajout d'instructions de journalisation à votre application

Les instructions de journalisation ajoutent les messages que vous spécifiez au journal. L'ajout d'instructions de journalisation à certains endroits du code permet au développeur de consulter les valeurs, les chemins d'exécution et les exceptions. Par exemple, l'instruction de journalisation suivante ajoute les termes "" MainActivity "et" "Hello World" ":

`Log.d (" MainActivity "," Hello World ");`

Voici les éléments de cette déclaration:

* `Log`: la classe [ Log](http://developer.android.com/reference/android/util/Log.html) pour l'envoi de messages de journal au volet**Logcat**.
* `d`: Le paramètre de niveau * Log` du journal Debug**pour filtrer les messages du journal s’affiche dans le volet**Logcat**. Les autres niveaux de journalisation sont `e` pour**Error**,` w` pour**Warn**et `i` pour**Info**. Vous affectez un niveau de journalisation afin de pouvoir filtrer les messages de journalisation à l'aide du menu déroulant situé au centre du volet**Logcat**.
* `" MainActivity "`: le premier argument est une balise qui peut être utilisée pour filtrer les messages dans le volet**Logcat**. Cette balise est généralement le nom de l'activité qui a généré le message. Cependant, vous pouvez nommer la balise tout ce qui vous est utile pour le débogage.
* `" Hello world "`: Le deuxième argument est le message réel.

Par convention, les balises de journal sont définies comme constantes pour le `Activity`:

    privé statique final String LOG_TAG = MainActivity.class.getSimpleName ();

Utilisez la constante dans les instructions de journalisation:

    Log.d (LOG_TAG, "Hello World");

Après avoir ajouté l'instruction `Log.d` ci-dessus, procédez comme suit pour afficher le message du journal:

1. Si le volet**Logcat**n'est pas déjà ouvert, cliquez sur l'onglet**Logcat**au bas d'Android Studio pour l'ouvrir.
2. Modifiez le niveau `Log` dans le volet**Logcat**en**Debug**. (Vous pouvez également laisser le niveau `Log` comme**Verbose**, car il y a si peu de messages de log.)
3. Exécutez votre application sur un périphérique virtuel.

Le message suivant devrait apparaître dans le volet**Logcat**:

    11-24 14: 06: 59,001 4696-4696 /? D/MainActivity: Bonjour tout le monde


### En savoir plus

Documentation d'Android Studio:

* [Page de téléchargement d'Android Studio](http://developer.android.com/sdk/index.html)
* [Meet Android Studio](http://developer.android.com/tools/studio/index.html)
* [Lire et écrire des journaux](http://developer.android.com/tools/debugging/debugging-log.html)
* [Gestionnaire de périphériques virtuels Android (AVD)](http://developer.android.com/tools/devices/managing-avds.html)
* [App Manifest](http://developer.android.com/guide/topics/manifest/manifest-intro.html)
* [Configurez votre build](https://developer.android.com/studio/build/index.html)
* Classe [[Log](https://developer.android.com/reference/android/util/Log.html)
* [Configurer les variantes de construction](https://developer.android.com/studio/build/build-variants.html)
* [Créer et gérer des périphériques virtuels](https://developer.android.com/studio/run/managing-avds.html)
* [Signer votre application](https://developer.android.com/studio/publish/app-signing.html)
* [Réduisez votre code et vos ressources](https://developer.android.com/studio/build/shrink-code.html)

Guide de l'API Android, section "Développement":

* [Introduction à Android](https://developer.android.com/guide/index.html)
* [Architecture de la plateforme](https://developer.android.com/guide/platform/index.html)
* [Présentation de l'interface utilisateur](https://developer.android.com/guide/topics/ui/overview.html)
* [Versions de plate-forme](http://developer.android.com/about/dashboards/index.html)
* [Prise en charge de différentes versions de plate-forme](https://developer.android.com/training/basics/supporting-devices/platforms.html)
* [Prise en charge de plusieurs écrans](https://developer.android.com/guide/practices/screens_support.html)

Autres:

* Wikipedia: [Résumé de l'historique de la version Android](https://en.wikipedia.org/wiki/Android_version_history)
* [Syntaxe Groovy](http://groovy-lang.org/syntax.html)
* [Comment installer Java?](Https://java.com/en/download/help/download_options.xml)
* [Installation du logiciel JDK et configuration de JAVA_HOME](https://docs.oracle.com/cd/E19182-01/820-7851/inst_cli_jdk_javahome_t/)
* [Site Gradle](https://gradle.org/)
* [Page Wikipedia de Gradle](https://en.wikipedia.org/wiki/Gradle)


## Interface Utilisateur : Mise en page et Ressources

**Contenu:**


* [Vues](#a)
* [L'éditeur de mise en page](#b)
* [Éditer XML directement](#c)
* [Fichiers de ressources](#d)
* <div aux="Répondre" clics="" sur="" la="" vue="">
  <div id="e"></div>
</div>
* [Travaux pratiques liés](#f)
* [En savoir plus](#g)

Ce chapitre décrit la présentation de l'interface utilisateur de l'écran et des autres ressources que vous avez créées pour votre application, ainsi que le code que vous utiliseriez pour répondre au toucher d'un élément de l'interface utilisateur par l'utilisateur.

### Vues (Views)

L'interface utilisateur est constituée d'une hiérarchie d'objets appelée _views_ - chaque élément de l'écran est un [View](https://developer.android.com/reference/android/view/View.html). La classe `View` représente le bloc de construction de base pour tous les composants d'interface utilisateur et la classe de base pour les classes qui fournissent des composants d'interface utilisateur interactifs tels que des boutons, des cases à cocher et des champs de saisie de texte.

Une `Vue` (View) a un emplacement, exprimé par une paire de coordonnées de gauche et du haut, et deux dimensions, exprimée par une largeur et une hauteur. L'unité pour l'emplacement et les dimensions est le pixel indépendant de la densité (dp).

Le système Android fournit des centaines de sous-classes `View` prédéfinies. Les sous-classes `View` couramment utilisées et décrites dans plusieurs leçons comprennent:

*   [TextView](http://developer.android.com/reference/android/widget/TextView.html) pour afficher du texte
*   [EditText](https://developer.android.com/reference/android/widget/EditText.html) pour permettre à l'utilisateur de saisir et de modifier du texte
*   [Button](https://developer.android.com/reference/android/widget/Button.html) et d'autres éléments cliquables (tels que [RadioButton](https://developer.android.com/reference/android/widget/RadioButton.html), [CheckBox](https://developer.android.com/reference/android/widget/CheckBox.html) et [Spinner](https://developer.android.com/reference/android/widget/Spinner.html)) pour fournir un comportement interactif
*   [ScrollView](https://developer.android.com/reference/android/widget/ScrollView.html) et [RecyclerView](https://developer.android.com/reference/android/support/v7/widget/RecyclerView.html) pour afficher les éléments défilables
*   [ImageView](https://developer.android.com/reference/android/widget/ImageView.html) pour afficher des images
*   [ConstraintLayout](https://developer.android.com/reference/android/support/constraint/ConstraintLayout.html) et [LinearLayout](https://developer.android.com/reference/android/widget/LinearLayout.html) pour contenir d’autres vues et les positionner.

Vous pouvez définir un `View` (vue) pour qu'il apparaisse à l'écran et réponde lorsque vous appuyez sur un utilisateur.
Un `View` (vue) peut également être défini pour accepter la saisie de texte ou pour être invisible jusqu'à ce que nécessaire.

Vous pouvez spécifier des éléments `View` dans les fichiers de ressources de mise en page. Les ressources de mise en page sont écrites en XML et répertoriées dans le dossier**layout**du dossier**res**du volet**Projet>Android**.

### Groupes ViewGroup

Les éléments `View` peuvent être regroupés dans un [ViewGroup](https://developer.android.com/reference/android/view/ViewGroup.html), qui fait office de conteneur. La relation est parent-enfant, dans laquelle le _parent_ est un `ViewGroup` et le _child_ est un` View` ou un autre `ViewGroup`. Les groupes `ViewGroup` couramment utilisés sont les suivants:

* [ConstraintLayout](https://developer.android.com/reference/android/support/constraint/ConstraintLayout.html): groupe qui place des éléments d'interface utilisateur (éléments enfant `View`) à l'aide de connexions de contrainte à d'autres éléments et aux bords de la mise en page (parent `View`).
* [ScrollView](https://developer.android.com/reference/android/widget/ScrollView.html): groupe qui contient un autre élément` View` enfant et permet de faire défiler l'élément enfant `View`.
* [RecyclerView](https://developer.android.com/reference/android/support/v7/widget/RecyclerView.html): un groupe contenant une liste d'autres éléments` View` ou de groupes `ViewGroup` et permet de les faire défiler en ajoutant et en supprimant dynamiquement les éléments `View` de l’écran.

### Layout ViewGroup groups

Les éléments `View` pour un écran sont organisés dans une hiérarchie.
À la racine de cette hiérarchie se trouve un [ViewGroup](https://developer.android.com/reference/android/view/ViewGroup.html) qui contient la disposition de l'écran entier. Le groupe `ViewGroup` peut contenir des éléments enfant` View` ou d'autres groupes `ViewGroup`, comme indiqué dans la figure suivante:

![La hiérarchie des vues](images/dg_viewgroup_hierarchy.png)

Dans la figure ci-dessus:

1. Le _root_ `ViewGroup`.
2. Le premier ensemble d'éléments `View` enfants et de groupes` ViewGroup` dont le parent est la racine.

Certains groupes `ViewGroup` sont désignés par _layouts_ car ils organisent les éléments enfant` View` de manière spécifique et sont généralement utilisés en tant que racine `ViewGroup`. Quelques exemples de mises en page sont:

* [ConstraintLayout](http://tools.android.com/tech-docs/layout-editor): groupe d’éléments enfants` View` utilisant des contraintes, des arêtes et des directives pour contrôler le positionnement des éléments par rapport à d'autres éléments dans la mise en page. `ConstraintLayout` a été conçu pour faciliter le clic sur les éléments` View` et les faire glisser dans l'éditeur de disposition.
* [LinearLayout](https://developer.android.com/reference/android/widget/LinearLayout.html): un groupe d'éléments enfant` View` positionnés et alignés horizontalement ou verticalement.
* [RelativeLayout](https://developer.android.com/reference/android/widget/RelativeLayout.html): groupe d’éléments enfants` View` dans lesquels chaque élément est positionné et aligné par rapport aux autres éléments de la liste. `ViewGroup`. En d'autres termes, les positions des éléments `View` de l'enfant peuvent être décrites les unes par rapport aux autres ou par rapport au` ViewGroup` parent.
* [TableLayout](https://developer.android.com/reference/android/widget/TableLayout.html): un groupe d'éléments enfant` View` organisés en rangées et en colonnes.
* [FrameLayout](https://developer.android.com/reference/android/widget/FrameLayout.html): un groupe d'éléments enfant` View` dans une pile. `FrameLayout` est conçu pour bloquer une zone de l'écran pour en afficher un` Voir`. Les éléments `View` des enfants sont dessinés dans une pile, avec le dernier enfant ajouté en haut. La taille de `FrameLayout` est la taille de son plus grand élément enfant` View`.
* [GridLayout](https://developer.android.com/reference/android/widget/GridLayout.html): groupe qui place ses éléments enfants` View` dans une grille rectangulaire qui peut être parcourue. ![Représentations visuelles des mises en page](images/dg_common_layouts_visual_rep.png "Représentations visuelles des mises en page")

> Positive
> : pour en savoir plus sur les différents types de disposition dans [Objets de mise en forme courants](https://developer.android.com/guide/topics/ui/layout-objects.html).

Un exemple simple de `LinearLayout` avec des éléments enfant` View` est présenté ci-dessous sous forme de diagramme du fichier de présentation (`activity_main.xml`), accompagné d'un diagramme de hiérarchie (en haut à droite) et d'une capture d'écran de la présentation finale ( en bas à droite).

![Concept de mise en page (à gauche), Hiérarchie des vues (à droite, en haut) et mise en page finie (à droite, en bas)]](images/dg_layout_diagram_and_hierarchy.png ")

Dans la figure ci-dessus:

1. `LinearLayout`, la racine` ViewGroup`, contient tous les éléments enfants `View` dans une orientation verticale.
2. `Button` (` button_toast`). Le premier élément `View` de l'enfant apparaît en haut de l'élément` LinearLayout`.
3. `TextView` (` show_count`). Le deuxième élément `View` de l'enfant apparaît sous le premier élément` View` de l'enfant dans `LinearLayout`.
4. `Button` (` button_count`). Le troisième élément `View` de l'enfant apparaît sous le deuxième élément` View` de l'enfant dans `LinearLayout`.

La hiérarchie des dispositions peut devenir complexe pour une application qui affiche de nombreux éléments `View` sur un écran. Il est important de comprendre la hiérarchie, car cela affecte la visibilité des éléments `View` et l'efficacité de leur dessin.

> Positive
> : vous pouvez explorer la hiérarchie de disposition de votre application à l'aide de [Visionneuse de hiérarchie](https://developer.android.com/studio/profile/hierarchy-viewer-walkthru.html). Il affiche une arborescence de la hiérarchie et vous permet d'analyser les performances des éléments `View` sur un appareil Android. Les problèmes de performances sont traités dans un chapitre ultérieur.

### L'éditeur de disposition (layout editor)

Vous définissez des mises en page dans l'éditeur de mise en page ou en entrant du code XML.

L'éditeur de disposition affiche une représentation visuelle du code XML. Vous pouvez faire glisser des éléments `View` dans le volet de conception ou de plans, puis organiser, redimensionner et spécifier leurs attributs. Vous voyez immédiatement l'effet des modifications que vous apportez.

Pour utiliser l'éditeur de disposition, double-cliquez sur le fichier de disposition XML (**activity_main.xml**). L'éditeur de disposition apparaît avec l'onglet**Dessin**en bas en surbrillance. (Si l'onglet**Texte**est mis en surbrillance et que vous voyez du code XML, cliquez sur l'onglet**Conception**.) Pour le modèle d'activité vide, la disposition est celle indiquée dans la figure ci-dessous.

![Exploring Android Studio](images/as_activity_main_in_project_pane_annot.png)

1. Fichier de mise en page XML (**activity_main.xml**).
2. Onglets**Conception**et**Texte**. Cliquez sur**Design**pour afficher l'éditeur de disposition ou sur**Texte**pour afficher le code XML.
3.**Palette**volet. Le volet Palette fournit une liste des éléments de l'interface utilisateur et des dispositions. Ajoutez un élément ou une mise en page à l'interface utilisateur en le faisant glisser dans le volet de conception.
4.**Arbre des composants**. Le volet Arborescence des composants affiche la hiérarchie de la disposition. Cliquez sur un élément `View` ou` ViewGroup` dans ce volet pour le sélectionner. Les éléments `View` sont organisés dans une arborescence de parents et d'enfants, dans laquelle un enfant hérite des attributs de son parent. Dans la figure ci-dessus, le `TextView` est un enfant du` ConstraintLayout`.
5. Conception et plan des vitres. Faites glisser les éléments `View` du volet**Palette**vers le volet dessin ou blueprint pour les positionner dans la présentation. Dans la figure ci-dessus, la mise en page montre un seul élément: un `TextView` qui affiche" Hello World ".
6.**Attributs**onglet. Cliquez sur**Attributs**pour afficher le volet**Attributes**permettant de définir les attributs d'un élément `View`.

### Barres d'outils (Layout editor toolbars)

Les barres d'outils de l'éditeur de disposition proposent des boutons permettant de configurer votre disposition et de modifier son apparence. La barre d'outils supérieure vous permet de configurer l'apparence de l'aperçu de la disposition dans l'éditeur de disposition:

![Barre d'outils supérieure de l'éditeur de disposition](images/as_constraint_toolbar1_annot.png)

La figure ci-dessus montre la barre d'outils supérieure de l'éditeur de disposition:

1.**Sélectionnez la surface de conception**: sélectionnez**Conception**pour afficher un aperçu couleur des éléments d'interface utilisateur de votre mise en page, ou**Plan**pour afficher uniquement les contours des éléments. Pour voir les deux panneaux côte à côte, sélectionnez**Design + Blueprint**.
2.**Orientation dans l'éditeur**: sélectionnez**Portrait**ou**Paysage**pour afficher l'aperçu dans une orientation verticale ou horizontale. Le paramètre d'orientation vous permet de prévisualiser les orientations de la mise en page sans exécuter l'application sur un émulateur ou un périphérique. Pour créer d'autres mises en page, sélectionnez**Créer une variation de paysage**ou d'autres variantes.
3.**Device in Editor**: sélectionnez le type de périphérique (téléphone/tablette, Android TV ou Android Wear).
4.**Version de l'API dans l'éditeur**: Sélectionnez la version d'Android à utiliser pour afficher l'aperçu.
5.**Thème dans l'éditeur**: sélectionnez un thème (tel que**AppTheme**) à appliquer à l'aperçu.
6.**Locale in Editor**: sélectionnez la langue et les paramètres régionaux de l'aperçu. Cette liste affiche uniquement les langues disponibles dans les ressources de chaîne (voir la leçon sur la localisation pour savoir comment ajouter des langues). Vous pouvez également sélectionner**Preview as Right To Left**pour voir la mise en page comme si une langue RTL avait été choisie.

L'éditeur de disposition propose également une deuxième barre d'outils qui vous permet de configurer l'apparence des éléments de l'interface utilisateur dans un `ConstraintLayout` et d'effectuer un zoom avant et arrière sur l'aperçu:

![Barre d'outils d'édition ConstraintLayout](images/as_constraint_toolbar2_annot.png)

La figure ci-dessus montre la barre d'outils d'édition `ConstraintLayout`:

1.**Afficher**: sélectionnez**Afficher les contraintes**et**Afficher les marges**pour les afficher dans l'aperçu ou pour ne plus les afficher.
2.**Connexion automatique**: Activer ou désactiver la connexion automatique. Lorsque la connexion automatique est activée, vous pouvez faire glisser n'importe quel élément (tel qu'un `Button`) vers n'importe quelle partie d'une mise en page pour générer des contraintes par rapport à la mise en page parent.
3.**Effacer toutes les contraintes**: Efface toutes les contraintes de la présentation.
4.**Inférer les contraintes**: Créer des contraintes par inférence.
5.**Marges par défaut**: définissez les marges par défaut.
6.**Pack**: Pack ou développez les éléments sélectionnés.
7.**Align**: Aligne les éléments sélectionnés.
8.**Directives**: Ajoutez des directives verticales ou horizontales.
9. Commandes de zoom: Zoom avant ou arrière.

### Utilisation de ConstraintLayout

L'éditeur de disposition offre davantage de fonctionnalités dans l'onglet**Design**lorsque vous utilisez un `ConstraintLayout`, y compris des descripteurs pour la définition de contraintes.

Une contrainte est une connexion ou un alignement sur un autre élément de l'interface utilisateur, sur la disposition parente ou sur une ligne directrice invisible. Chaque contrainte apparaît sous la forme d'une ligne s'étendant à partir d'une poignée circulaire. Une fois que vous avez sélectionné un élément de l'interface utilisateur dans le volet**Arborescence des composants**ou que vous avez cliqué dessus dans l'éditeur de disposition, il affiche une poignée de redimensionnement à chaque coin et une poignée de contrainte circulaire au milieu de chaque côté.

![La contrainte et le redimensionnement des poignées sur les vues](images/as_layout_constraint_2_handles_annot.png)

La figure ci-dessus montre les poignées de contrainte et de redimensionnement des éléments `View` d'une présentation:

1.**Poignée de redimensionnement**.
2.**Ligne de contrainte et poignée**. Dans la figure, la contrainte aligne le côté gauche du bouton**Toast**sur le côté gauche de la présentation.
3.**Poignée de contrainte**sans ligne de contrainte.
4.**Poignée de base**. La poignée de ligne de base aligne la ligne de base du texte d'un élément sur la ligne de base du texte d'un autre élément.

Dans les panneaux de plans ou de conception, les poignées suivantes apparaissent sur l'élément `TextView`:

***Poignée de contrainte**: pour créer une contrainte, cliquez sur une poignée de contrainte, représentée par un cercle de chaque côté d'un élément. Ensuite, faites glisser le cercle vers une autre poignée de contrainte ou vers une limite parent. Une ligne en zigzag représente la contrainte.

![Poignée de contrainte](images/handles.png)

***Poignée de redimensionnement**: vous pouvez faire glisser les poignées de redimensionnement carrées pour redimensionner l'élément. Lors du déplacement, la poignée se transforme en un coin incliné. ![Identifiant de contrainte](images/handle_resize.png "Identifiant de contrainte")

Vous pouvez faire glisser les poignées de redimensionnement sur chaque coin de l'élément d'interface pour le redimensionner, mais codez ainsi les dimensions en largeur et en hauteur, ce que vous devriez éviter pour la plupart des éléments, car les dimensions codées en dur ne s'adaptent pas à différentes densités d'écran.

#### Contraindre un élément de l'interface utilisateur

Pour ajouter une contrainte à un élément de l'interface utilisateur, cliquez sur la poignée circulaire et faites glisser une ligne vers un autre élément ou sur le côté d'une présentation, comme indiqué dans les deux figures animées ci-dessous. Pour supprimer une contrainte d'un élément, cliquez sur la poignée circulaire. ![Supprimer et ajouter une contrainte](images/hello_world_textview_constraints.gif "Supprimer et ajouter une contrainte")

![](images/hello_toast7_drag_buttons_constrain.gif)

Les contraintes que vous définissez dans l'éditeur de mise en page sont créées sous forme d'attributs XML, que vous pouvez voir dans l'onglet**Texte**, comme décrit dans la section "[Édition de XML directement](# xml)" dans ce chapitre. Par exemple, le code XML suivant est créé en contraignant le haut d'un élément au sommet de son parent:

    app: layout_constraintTop_toTopOf = "parent"

#### Utilisation d'une contrainte de base

Vous pouvez aligner un élément d'interface utilisateur contenant du texte, tel qu'un `TextView` ou` Button`, avec un autre élément d'interface utilisateur contenant du texte. Une contrainte de base vous permet de contraindre les éléments afin que les lignes de base du texte correspondent. Sélectionnez l'élément d'interface utilisateur contenant du texte, puis placez le pointeur de la souris sur l'élément jusqu'à ce que le bouton de contrainte de ligne de base
![](images/ic_ab_baseline_icon.png) apparaît sous l'élément.

Cliquez sur le bouton Contrainte de ligne de base. La poignée de la ligne de base apparaît et clignote en vert, comme indiqué dans la figure animée. Faites glisser une ligne de contrainte de ligne de base sur la ligne de base de l'autre élément d'interface utilisateur.
*![](images/hello_toast8_align_baselines.gif)

> Positive
> : Pour obtenir un didacticiel détaillé sur l'utilisation de `ConstraintLayout`, voir [Utilisation de ConstraintLayout pour concevoir vos vues](https://codelabs.developers.google.com/codelabs/constraint-layout/index.html).


### Utilisation du volet Attributs

Le volet**Attributs**permet d'accéder à tous les attributs XML que vous pouvez affecter à un élément de l'interface utilisateur. Vous pouvez trouver les attributs (appelés propriétés) communs à toutes les vues dans la documentation de la classe [View](http://developer.android.com/reference/android/view/View.html).

Pour afficher le volet**Attributs**, cliquez sur l'onglet**Attributs**situé à droite de l'éditeur de présentation. Le volet**Attributs**inclut un panneau de dimensionnement carré appelé _view inspector_. Les symboles à l'intérieur de l'inspecteur de vue représentent les paramètres de hauteur et de largeur. ![Panneau de dimensionnement dans le volet Attributs](images/as_layout_width_height_box_annot.png)

La figure ci-dessus montre le volet**Attributs**:

1.**Contrôle de la taille de la vue verticale**. Le contrôle de taille verticale, qui apparaît en haut et en bas de l'inspecteur de vue, spécifie la propriété `layout_height`. Les angles indiquent que ce contrôle de taille a la valeur `wrap_content`, ce qui signifie que l’élément UI s’agrandit verticalement selon les besoins pour s’adapter à son contenu. Le "8" indique une marge standard définie à 8 dp.
2.**Contrôle de la taille de la vue horizontale**. Le contrôle de taille horizontale, qui apparaît à gauche et à droite de l'inspecteur de vue, spécifie le `layout_width`. Les angles indiquent que ce contrôle de taille est défini sur `wrap_content`, ce qui signifie que l'élément d'interface utilisateur se dilate horizontalement si nécessaire pour s'adapter à son contenu, jusqu'à une marge de 8 dp.
3.**Attributs**bouton de fermeture du volet. Cliquez pour fermer le volet.

Les attributs `layout_width` et` layout_height` dans le volet**Attributs**changent lorsque vous modifiez les commandes de taille horizontale et verticale de l'inspecteur. Ces attributs peuvent prendre l’une des trois valeurs d’un `ConstraintLayout`:

* Le paramètre `match_constraint` développe l'élément d'interface utilisateur pour remplir son parent en largeur ou en hauteur, jusqu'à une marge, si une marge est définie. Le parent dans ce cas est le `ConstraintLayout`.
* Le paramètre `wrap_content` réduit l'élément de l'interface utilisateur à la taille de son contenu. S'il n'y a pas de contenu, l'élément devient invisible.
* Pour spécifier une taille fixe ajustée à la taille de l'écran du périphérique, définissez un nombre de `dp` ([pixels indépendants de la densité]](https://developer.android.com/training/multiscreen/screendensities.html)). Par exemple, `16dp` signifie 16 pixels indépendants de la densité.


> Positive
> : Si vous modifiez l'attribut `layout_width` à l'aide de son menu contextuel, l'attribut` layout_width` est défini sur zéro car il n'y a pas de dimension définie. Ce paramètre est identique à `match_constraint` - l'élément d'interface utilisateur peut être développé autant que possible pour respecter les contraintes et les paramètres de marge.

Le volet**Attributs**permet d'accéder à tous les attributs que vous pouvez affecter à un élément `View`. Vous pouvez entrer des valeurs pour chaque attribut, telles que les attributs `android: id`,` background`, `textColor` et` text`.

### Création de variantes de mise en page pour les orientations et les appareils

Vous pouvez prévisualiser la mise en page d'une application avec une orientation horizontale et avec différents appareils, sans avoir à exécuter l'application sur un émulateur ou un appareil.

Pour prévisualiser la mise en page pour une orientation différente, cliquez sur le bouton**Orientation dans l'éditeur**![Bouton Orientation dans l'éditeur](images/ic_orientation_in_editor_button.png) dans la barre d'outils supérieure. Pour afficher la mise en page dans une orientation horizontale, sélectionnez**Basculer en paysage**. Pour revenir à l'orientation verticale, sélectionnez**Basculer vers Portrait**.

Vous pouvez également prévisualiser la mise en page pour différents appareils. Cliquez sur le bouton**Device in Editor**
![Bouton Périphérique dans l'éditeur](images/ic_device_in_editor_button.png) dans la barre d'outils supérieure et sélectionnez un autre périphérique dans le menu déroulant. Par exemple, sélectionnez**Nexus 4**,**Nexus 5**, puis**Pixel**pour voir les différences entre les aperçus.


Pour créer une variante de la mise en page strictement pour l'orientation horizontale, en laissant la disposition uniquement verticale: cliquez sur le bouton**Orientation dans l'éditeur**et sélectionnez**Créer une variante de paysage**. Une nouvelle fenêtre d'éditeur s'ouvre avec l'onglet**land/activity_main.xml**montrant la mise en page pour l'orientation paysage (horizontale). Vous pouvez modifier cette disposition, qui est spécifiquement destinée à l'orientation horizontale, sans modifier l'orientation du portrait (vertical) d'origine.

Dans le volet**Projet>Android**, examinez le répertoire**res>layout**. Vous voyez qu'Android Studio crée automatiquement la variante pour vous, appelée `activity_main.xml (land)`.

![Le fichier de la variante de présentation dans le répertoire de présentation](images/as_layout_landscape_xml.png)

Pour créer une variante de présentation pour les écrans de la taille d'une tablette, cliquez sur le bouton**Orientation dans l'éditeur**et sélectionnez**Créer une variante de présentation très large**. Une nouvelle fenêtre d'éditeur s'ouvre avec l'onglet**xlarge/activity_main.xml**indiquant la disposition d'un périphérique de la taille d'une tablette. L’éditeur choisit également une tablette, telle que le Nexus 9 ou le Nexus 10, pour l’aperçu. Dans le volet**Projet>Android**, examinez le répertoire**res>layout**. Vous voyez qu'Android Studio crée automatiquement la variante pour vous, appelée `activity_main.xml (xlarge)`. Vous pouvez modifier cette présentation, spécialement destinée aux tablettes, sans modifier les autres dispositions.

<a id="xml"></a>

### Édition directe de XML

Il est parfois plus rapide et plus facile d’éditer directement le code XML, en particulier lorsqu’il est copié et collé pour des vues similaires.

Pour afficher et modifier le code XML, ouvrez le fichier de présentation XML. L'éditeur de disposition apparaît avec l'onglet**Dessin**en bas en surbrillance. Cliquez sur l'onglet**Texte**pour voir le code XML. Ce qui suit montre le code XML pour un `LinearLayout` avec deux éléments` Button` avec un `TextView` au milieu:

    <LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
        xmlns:app="http://schemas.android.com/apk/res-auto"
        xmlns:tools="http://schemas.android.com/tools"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:orientation="vertical"
        tools:context="com.example.android.hellotoast.MainActivity">

        <Button
            android:id="@+id/button_toast"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:layout_marginEnd="8dp"
            android:layout_marginStart="8dp"
            android:layout_marginTop="8dp"
            android:background="@color/colorPrimary"
            android:onClick="showToast"
            android:text="@string/button_label_toast"
            android:textColor="@android:color/white" />

        <TextView
            android:id="@+id/show_count"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:gravity="center_vertical"
            android:layout_marginBottom="8dp"
            android:layout_marginEnd="8dp"
            android:layout_marginStart="8dp"
            android:layout_marginTop="8dp"
            android:background="#FFFF00"
            android:text="@string/count_initial_value"
            android:textAlignment="center"
            android:textColor="@color/colorPrimary"
            android:textSize="160sp"
            android:textStyle="bold"
            android:layout_weight="1"/>

        <Button
            android:id="@+id/button_count"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:layout_marginBottom="8dp"
            android:layout_marginEnd="8dp"
            android:layout_marginStart="8dp"
            android:background="@color/colorPrimary"
            android:onClick="countUp"
            android:text="@string/button_label_count"
            android:textColor="@android:color/white" />
    </LinearLayout>

### Attributs XML (propriétés de la vue)

Les vues ont _properties_ qui définissent l'emplacement d'une vue à l'écran, sa taille, son rapport avec d'autres vues et sa réponse aux entrées de l'utilisateur. Lors de la définition de vues dans XML ou dans le volet**Attributs**de l'éditeur de présentation, les propriétés sont appelées _attributes_.

Par exemple, dans la description XML suivante d'un `TextView`, les symboles android: id, android: layout_width, android: layout_height, android: background, sont des attributs XML traduits automatiquement en mode` TextView `propriétés:

    <TextView
           android: id = "@ + id/show_count"
           android: layout_width = "match_parent"
           android: layout_height = "wrap_content"
           android: background = "@ color/myBackgroundColor"
           android: textStyle = "bold"
           android: text = "@ string/count_initial_value" />

Les attributs prennent généralement cette forme:

`android:` _attribute_name_ = `" `_value_`" `

_Nom_attribut_ est le nom de l'attribut. La _value_ est une chaîne avec la valeur de l'attribut. Par exemple:

    android: textStyle = "bold"

Si _value_ est une ressource, telle qu'une couleur, le symbole `@` spécifie le type de ressource. Par exemple:

    android: background = "@ color/myBackgroundColor"

L'attribut background est défini sur la ressource de couleur identifiée comme `myBackgroundColor`, qui est déclarée comme` # FFF043`. Les ressources de couleur sont décrites dans [Attributs liés au style](# style_related) dans ce chapitre.

Chaque `View` et` ViewGroup` supporte sa propre variété d'attributs XML:

* Certains attributs sont spécifiques à une sous-classe `View`. Par exemple, la sous-classe `TextView` prend en charge l'attribut` textSize`. Tous les éléments qui étendent la sous-classe `TextView` héritent de ces attributs spécifiques à la sous-classe.
* Certains attributs sont communs à tous les éléments `View`, car ils sont hérités de la classe racine [ View](https://developer.android.com/reference/android/view/View.html). L'attribut `android: id` en est un exemple.

Pour obtenir une description des attributs spécifiques, consultez la section de présentation de la documentation de la classe [View](https://developer.android.com/reference/android/view/View.html).

### Identifier une vue

Pour identifier une `View` de manière unique et la référencer à partir de votre code, vous devez lui donner un` id`. L'attribut `Android: id` vous permet de spécifier un` id` unique, un identifiant de ressource pour un `View`.

Par exemple:

    android: id = "@ + id/button_count"

La partie `@ + id/button_count` de l'attribut crée un` id` appelé `button_count` pour un` Button` (une sous-classe de `View`). Vous utilisez le symbole plus (`+`) pour indiquer que vous créez un nouveau `id`.

### Référencer une vue

Pour faire référence à un identifiant de ressource existant, omettez le symbole plus (`+`). Par exemple, pour faire référence à un `View` par son` id` dans l'attribut _another_, tel que `android: layout_toLeftOf` (décrit dans la section suivante) pour contrôler la position d'un` View`, vous devez utiliser:

    android: layout_toLeftOf = "@ id/show_count"

Dans l'attribut ci-dessus, `@ id/show_count` fait référence à la` vue` avec l'identifiant de ressource `show_count`. L'attribut positionne l'élément à "à gauche de" la vue `show_count``.

### Positionnement d'une vue

Certains attributs de positionnement liés à la présentation sont requis pour un `View` ou un` ViewGroup`, et apparaissent automatiquement lorsque vous ajoutez le `View` ou le` ViewGroup` à la présentation XML.

#### Positionnement LinearLayout

`LinearLayout` est requis pour que ces attributs soient définis:

* [android: layout_width](https://developer.android.com/reference/android/view/ViewGroup.LayoutParams.html#attr_android:layout_width)
* [android: layout_height](https://developer.android.com/reference/android/view/ViewGroup.LayoutParams.html#attr_android:layout_height)
* [android: orientation](https://developer.android.com/reference/android/widget/LinearLayout.html#attr_android:orientation)

Les attributs `android: layout_width` et` android: layout_height` peuvent prendre l'une des trois valeurs suivantes:

* `match_parent` développe l'élément d'interface utilisateur pour remplir son parent en largeur ou en hauteur. Lorsque LinearLayout est la racine `ViewGroup`, il se développe à la taille de l'écran du périphérique. Pour un élément d'interface utilisateur situé dans une racine, `ViewGroup`, il se développe à la taille du parent` ViewGroup`.
* `wrap_content` réduit l'élément d'interface utilisateur à la taille de son contenu. S'il n'y a pas de contenu, l'élément devient invisible.
* Utilisez un nombre fixe de `dp` ([pixels indépendants de la densité](https://developer.android.com/training/multiscreen/screendensities.html)) pour spécifier une taille fixe, ajustée à la taille d'écran du périphérique. . Par exemple, `16dp` signifie 16 pixels indépendants de la densité. Les pixels indépendants de la densité et les autres dimensions sont décrits dans la section "[Dimensions](# dimensions)" de ce chapitre.

Le `android: orientation` peut être:

* `horizontal`**:**Les vues sont disposées de gauche à droite.
* `vertical`**:**Les vues sont disposées de haut en bas.

Les autres attributs liés à la présentation incluent:

* `android: layout_gravity`: cet attribut est utilisé avec un élément d'interface utilisateur pour contrôler l'emplacement de l'élément dans son parent. Par exemple, l'attribut suivant centre l'élément d'interface utilisateur horizontalement dans le `ViewGroup` parent:

    android: layout_gravity = "center_horizontal"

* Le remplissage correspond à l'espace, mesuré en pixels indépendants de la densité, entre les bords de l'élément de l'interface utilisateur et le contenu de l'élément, comme indiqué dans la figure ci-dessous. ![Padding](images/dg_padding_annotated.png "Padding")

Dans la figure ci-dessus: (1) _Padding_ est l'espace entre les bords du `TextView` (lignes en pointillés) et le contenu du` TextView` (ligne continue). Le rembourrage n'est pas la même chose que _margin_, qui est l'espace entre le bord de la `View` et son parent.

La taille d'un `View` inclut son remplissage. Voici les attributs de remplissage couramment utilisés:

* `android: padding`: définit le remplissage des quatre bords.
* `android: paddingTop`: définit le remplissage du bord supérieur.
* `android: paddingBottom`: définit le remplissage du bord inférieur.
* `android: paddingLeft`: définit le remplissage du bord gauche.
* `android: paddingRight`: définit le remplissage du bord droit.
* `android: paddingStart`: définit le remplissage du début de la vue, en pixels. Utilisé à la place des attributs de remplissage énumérés ci-dessus, en particulier avec les vues longues et étroites.
* `android: paddingEnd`: définit le remplissage du bord de fin de la vue, en pixels. Utilisé avec `Android: paddingStart`.

> Positive
> : Pour voir tous les attributs XML pour un `LinearLayout`, voir la section Résumé du [ LinearLayout](https://developer.android.com/reference/android/widget/LinearLayout.html ) définition de classe. Autres modèles de racine, tels que [RelativeLayout](http://developer.android.com/guide/topics/ui/layout/relative.html) et [ AbsoluteLayout](https://developer.android.com /reference/android/widget/AbsoluteLayout.html), répertorie également ses attributs XML dans les sections Résumé.

#### Positionnement RelativeLayout

Un autre `Viewgroup` utile pour la présentation est [ RelativeLayout](https://developer.android.com/reference/android/widget/RelativeLayout.html), que vous pouvez utiliser pour positionner les éléments enfants `View` les uns par rapport aux autres ou au parent. Les attributs que vous pouvez utiliser avec `RelativeLayout` sont les suivants:

* [android: layout_toLeftOf](https://developer.android.com/reference/android/widget/RelativeLayout.LayoutParams.html#attr_android:layout_toLeftOf): positionne le bord droit de cette" vue "à gauche d'un autre `View` (identifié par son` ID`).
* [android: layout_toRightOf](https://developer.android.com/reference/android/widget/RelativeLayout.LayoutParams.html#attr_android:layout_toRightOf): positionne le bord gauche de cette« vue »à la droite d'un autre `View` (identifié par son` ID`).
* [android: layout_centerHorizontal](https://developer.android.com/reference/android/widget/RelativeLayout.LayoutParams.html#attr_android:layout_centerHorizontal): Centre cette` View` horizontalement dans son parent.
* [android: layout_centerVertical](https://developer.android.com/reference/android/widget/RelativeLayout.LayoutParams.html#attr_android:layout_centerVertical): centre cette` Voir`` verticalement dans son parent.
* [android: layout_alignParentTo`p](https://developer.android.com/reference/android/widget/RelativeLayout.LayoutParams.html#attr_android:layout_alignParentTop): positionne le bord supérieur de cette vue pour correspondre au sommet. bord du parent.
* [android: layout_alignParentBottom](https://developer.android.com/reference/android/widget/RelativeLayout.LayoutParams.html#attr_android:layout_alignParentBottom): positionne le bord inférieur de cette« vue »en regard du parent.

Pour obtenir une liste complète des attributs des éléments de sous-classe `View` et` View` dans un `RelativeLayout`, voir [ RelativeLayout.LayoutParams](https://developer.android.com/reference/android/widget/RelativeLayout.LayoutParams .html).


### Attributs liés au style

Vous spécifiez des attributs de style pour personnaliser l'apparence d'une `View`. Une vue qui ne possède pas d'attributs de style, tels que android: textColor, android: textSize, android: background, reprend les styles définis dans le thème de l'application.

Voici les attributs liés au style utilisés dans la leçon d'utilisation de l'éditeur de présentation:

* `android: background`: spécifie une couleur ou une ressource pouvant être dessinée à utiliser comme arrière-plan.
* `android: text`: Spécifie le texte à afficher dans la vue.
* `android: textColor`: spécifie la couleur du texte.
* `android: textSize`: Spécifie la taille du texte.
* `android: textStyle`: Spécifie le style du texte, tel que` bold`.


### Fichiers de ressources (Resource files)

Les fichiers de ressources permettent de séparer les valeurs statiques du code afin que vous n'ayez pas à modifier le code lui-même pour modifier les valeurs. Vous pouvez stocker toutes les chaînes, dispositions, dimensions, couleurs, styles et texte de menu séparément dans des fichiers de ressources.

Les fichiers de ressources sont stockés dans des dossiers situés dans le dossier `res` lors de l'affichage du volet Projet>Android. Ces dossiers incluent:

* `drawable`: Pour les images et les icônes
* `layout`: Pour les fichiers de ressources de présentation
* `menu`: Pour les éléments de menu
* `mipmap`: pour des collections pré-calculées et optimisées d'icônes d'application utilisées par le lanceur
* `values`: pour les couleurs, les dimensions, les chaînes et les styles (attributs de thème)

La syntaxe pour référencer une ressource dans une présentation XML est la suivante:

`@` _ _package_name_`: `_ _resource_type_` /` _ _ressource_name_

* _package_name_ est le nom du package dans lequel se trouve la ressource. Le nom du package n'est pas requis lorsque vous référencez des ressources stockées dans le dossier `res` de votre projet, car ces ressources proviennent du même package.
* _resource_type_ est la sous-classe `R` pour le type de ressource. Voir [Types de ressources](https://developer.android.com/guide/topics/resources/available-resources.html) pour plus d'informations sur les types de ressources et sur la manière de les référencer.
* _nom_source_ est soit le nom de la ressource sans l'extension, soit la valeur de l'attribut `android: name` dans l'élément XML.

Par exemple, l’instruction de présentation XML suivante définit l’attribut `android: text` sur une ressource` string`:

    android: text = "@ string/button_label_toast"

* _Package_name_ n'est pas inclus car la ressource est stockée dans le fichier `strings.xml` du projet.
* Le _resource_type_ est `string`.
* Le _nom_de_source_ est: `button_label_toast.`

Autre exemple: cette instruction de mise en page XML définit l'attribut `android: background` sur une ressource` color`, et comme la ressource est définie dans le projet (dans le fichier `colors.xml`), le _nom_package_ n'est pas spécifié:

    android: background = "@ color/colorPrimary"

Dans l'exemple suivant, l'instruction XML layout définit l'attribut `android: textColor` sur une ressource` color`. Cependant, la ressource n'est pas définie dans le projet mais fournie par Android. Vous devez donc spécifier le _package_name_, qui est `android`, suivi de deux points:

    android: textColor = "@ android: couleur/blanc"

> Positive
> : pour plus d'informations sur l'accès aux ressources à partir de code, voir [Accès aux ressources](http://developer.android.com/guide/topics/resources/accessing-resources.html). Pour les constantes de couleur Android, voir [Ressources Android standard R.color](http://developer.android.com/reference/android/R.color.html).


Le fait de conserver des valeurs telles que les chaînes et les couleurs dans des fichiers de ressources distincts facilite leur gestion, en particulier si vous les utilisez plusieurs fois dans vos mises en page.

Par exemple, il est essentiel de conserver les chaînes dans un fichier de ressources distinct pour la traduction et la localisation de votre application, de sorte que vous puissiez créer un fichier de ressources sous forme de chaîne pour chaque langue sans modifier votre code. Les fichiers de ressources pour les images, les couleurs, les dimensions et d'autres attributs sont utiles pour développer une application pour différentes tailles et orientations d'écran.

### Strings (ressources de chaîne)

Les ressources de chaîne se trouvent dans le fichier `strings.xml` (dans**res>values ​​**dans le volet**Project>Android**). Vous pouvez éditer ce fichier directement en l'ouvrant dans le panneau d'édition:

    <ressources>
        <string name = "app_name">Bonjour Toast </ string>
        <string name = "button_label_count">Count </ string>
        <string name = "button_label_toast">Toast </ string>
        <string name = "count_initial_value">0 </ string>
    </ressources>

Le `name` (par exemple,` button_label_count`) est le nom de la ressource que vous utilisez dans votre code XML, comme dans l'attribut suivant:

    android: text = "@ string/button_label_count"

La valeur de chaîne de ce `name` est le mot (` Count`) contenu dans les balises `<string></ string>`. (Vous n'utilisez pas de guillemets à moins que ceux-ci fassent partie de la valeur de la chaîne.)


### Extraire des chaînes de caractères vers des ressources (strings to resources)

Vous devez également utiliser _extract_ des chaînes codées en dur dans un fichier de présentation XML en ressources chaîne.

![Extraire une ressource chaîne](images/as_extract_string_resources.png)

![Nommer la ressource chaîne](images/as_extract_string_resources2.png)

Pour extraire une chaîne codée en dur dans une disposition XML, procédez comme suit, comme illustré dans la figure ci-dessus:

1. Cliquez sur la chaîne codée en dur et appuyez sur**Alt-Enter**sous Windows ou**Option-Return**sous Mac OS X.
2. Sélectionnez**Extraire la ressource de chaîne**.
3. Modifiez le**Nom de la ressource**pour la valeur de chaîne.

Vous pouvez ensuite utiliser le nom de la ressource dans votre code XML. Utilisez l'expression `" @ string/nom_ressource "` (guillemets inclus) pour faire référence à la ressource string:

    android: text = "@ string/button_label_count"

### Couleurs

Les ressources de couleur se trouvent dans le fichier `colors.xml` (à l'intérieur de**res>values ​​**dans le volet**Projet>Android**). Vous pouvez éditer ce fichier directement dans le panneau de l'éditeur:

    <ressources>
        <color name = "colorPrimary"># 3F51B5 </ color>
        <color name = "colorPrimaryDark"># 303F9F </ color>
        <color name = "colorAccent"># FF4081 </ color>
        <color name = "myBackgroundColor"># FFF043 </ color>
    </ ressources>

Le `name` (par exemple,` colorPrimary`) est le nom de la ressource que vous utilisez dans votre code XML:

    android: textColor = "@ color/colorPrimary"

La valeur de couleur de ce `name` est la valeur de couleur hexadécimale (` # 3F51B5`) incluse dans les balises `<color></ color>`. La valeur hexadécimale spécifie les valeurs rouge, verte et bleue (RVB). La valeur commence toujours par un caractère dièse (`#`), suivi des informations Alpha-Rouge-Vert-Bleu. Par exemple, la valeur hexadécimale pour le noir est # 000000, tandis que la valeur hexadécimale pour une variante du bleu du ciel est # 559fe3 \. Les valeurs de couleur de base sont répertoriées dans la documentation de classe [Couleur](https://developer.android.com/reference/android/graphics/Color.html).

La couleur `colorPrimary` est l'une des couleurs de base prédéfinies et est utilisée pour la barre d'applications. Dans une application de production, vous pouvez, par exemple, l'adapter à votre marque. L'utilisation des couleurs de base pour d'autres éléments d'interface utilisateur crée une interface utilisateur uniforme.

> Positive
> : Pour connaître la spécification de matériau utilisée pour les couleurs Android, voir [Style](https://material.google.com/style/color.html#) et [Utilisation du thème de matériau](https: // développeur .android.com/training/material/theme.html). Pour les valeurs hexadécimales de couleur commune, voir [Codes de couleur de couleur hexadécimale](http://www.color-hex.com/). Pour les constantes de couleur Android, voir [Ressources Android standard R.color](http://developer.android.com/reference/android/R.color.html).

Vous pouvez voir un petit bloc du choix de couleur dans la marge de gauche à côté de la déclaration de ressource de couleur dans `colors.xml`, ainsi que dans la marge de gauche à côté de l'attribut qui utilise le nom de la ressource dans le fichier XML de présentation.

![Blocs de couleur dans le fichier de ressources](images/as_color_block_in_colors_xml.png)

![Bloc de couleur dans le fichier de mise en page](images/as_color_block_in_layout.png)

> Positive
> : pour afficher la couleur dans une fenêtre contextuelle, activez la fonction de documentation Autopopup. Sélectionnez**Préférences>Editeur>Général>Achèvement du code**, puis sélectionnez l'option "Documentation Autopopup en (ms)". Vous pouvez ensuite passer votre curseur sur un nom de ressource de couleur pour voir la couleur.

### Dimensions

Pour faciliter la gestion des dimensions, vous devez les séparer de votre code, en particulier si vous devez ajuster votre mise en page pour des périphériques avec différentes densités d'écran. Le fait de séparer les dimensions du code facilite également le dimensionnement cohérent des éléments de l'interface utilisateur et la modification de la taille de plusieurs éléments en modifiant une ressource de dimension.

Les ressources de dimension se trouvent dans le fichier `dimens.xml` (à l'intérieur de**res>values ​​**dans le volet**Projet>Android**). Le fichier `dimens.xml` peut en réalité être un dossier contenant plusieurs fichiers` dimens.xml`, un pour chaque résolution d'écran du périphérique. Vous pouvez éditer chaque fichier `dimens.xml` directement:

    <ressources>
        <! - Marges d'écran par défaut, conformément aux directives de conception d'Android. ->
        <dimen name = "activity_horizontal_margin">16dp </ dimen>
        <dimen name = "activity_vertical_margin">16dp </ dimen>
        <dimen name = "my_view_width">300dp </ dimen>
        <dimen name = "count_taille_text">200sp </ dimen>
        <dimen name = "counter_height">300dp </ dimen>
    </ ressources>

Le `name` (par exemple,` activity_horizontal_margin`) est le nom de la ressource que vous utilisez dans le code XML:

    android: paddingLeft = "@ dimen/activity_horizontal_margin"

La valeur de ce `name` est la mesure (` 16dp`) incluse dans les balises `<dimen></ dimen>`.

Vous pouvez extraire des cotes de la même manière que des chaînes:

1. Cliquez sur la dimension codée en dur, puis appuyez sur**Alt-Enter**sous Windows ou sur**Option-Return**sous Mac OS X.
2. Sélectionnez**Extraire la ressource de dimension**.
3. Modifiez le**Nom de la ressource**pour la valeur de la dimension.

[Pixels indépendants de la densité](https://developer.android.com/training/multiscreen/screendensities.html) (`dp`) sont indépendants de la résolution de l'écran. Par exemple, `10px` (10 pixels fixes) a l'air beaucoup plus petit sur un écran de résolution supérieure, mais Android met à l'échelle 1`0dp` (10 pixels indépendants de l'appareil) pour un affichage correct sur des écrans de résolution différente. Les tailles de texte peuvent également être définies pour avoir une bonne apparence sur des écrans de résolution différents en utilisant les tailles _scaled-pixel_ (`sp`).

> Positive
> : Pour plus d'informations sur les unités `dp` et` sp`, voir [Prise en charge de différentes densités](http://developer.android.com/training/multiscreen/screendensities.html).

### Modes

Un style est une ressource qui spécifie des attributs communs tels que la hauteur, le remplissage, la couleur de la police, la taille de la police et la couleur de l'arrière-plan. Les styles sont destinés aux attributs qui modifient l'apparence de la vue.

Les styles sont définis dans le fichier `styles.xml` (dans**res>values ​​**dans le volet**Project>Android**). Vous pouvez éditer ce fichier directement. Les styles sont traités dans un chapitre ultérieur, avec la spécification de conception de matériau.

### Autres fichiers de ressources

Android Studio définit d'autres ressources couvertes dans d'autres chapitres:

* Images et icônes: Le dossier `drawable` fournit des ressources d’icône et d’image. Si votre application ne possède pas de dossier `drawable`, vous pouvez le créer manuellement dans le dossier` res`. Pour plus d'informations sur les ressources disponibles, voir [Ressources utiles](https://developer.android.com/guide/topics/resources/drawable-resource.html) dans la section Ressources d'application du Guide du développeur Android.
* Icônes optimisées: le dossier `mipmap` contient généralement des collections pré-calculées et optimisées d'icônes d'application utilisées par le lanceur. Développez le dossier pour voir que les versions des icônes sont stockées en tant que ressources pour différentes densités d'écran.
* Menus: Vous pouvez utiliser un fichier de ressources XML pour définir des éléments de menu et les stocker dans votre projet dans le dossier `menu`. Les menus sont décrits dans un chapitre ultérieur.

### Répondre aux clics d’affichage

Un événement _click_ se produit lorsque l'utilisateur appuie ou clique sur une `View` sur laquelle il est possible de cliquer, telle qu'un [ Button](https://developer.android.com/reference/android/widget/Button.html), [ImageButton` ](https://developer.android.com/reference/android/widget/ImageButton.html), [ImageView](https://developer.android.com/reference/android/widget/ImageView.html), ou [FloatingActionButton](https://developer.android.com/reference/android/support/design/widget/FloatingActionButton.html). Lorsqu'un tel événement se produit, votre code exécute une action. Pour que ce modèle fonctionne, vous devez:

* Ecrivez une méthode Java qui effectue l'action spécifique que vous souhaitez que l'application effectue lorsque cet événement se produit. Cette méthode est généralement appelée un gestionnaire d'événement.
* Associez cette méthode de gestionnaire d'événement à la `View` pour qu'elle s'exécute lorsque l'événement se produit.

### L'attribut onClick

Android Studio fournit un raccourci pour configurer une `View` cliquable et pour associer un gestionnaire d'événement à` View`: utiliser l'attribut `android: onClick` dans la présentation XML.

Par exemple, l'attribut XML suivant définit un `Button` sur lequel il est possible de cliquer, et définit` showToast () `en tant que gestionnaire d'événements:

    <Bouton
        android: id = "@ + id/button_toast"
        android: onClick = "showToast"

Lorsque l'utilisateur appuie sur le bouton `button_toast`, l'attribut` android: onClick` du bouton appelle la méthode `showToast ()`. Afin de travailler avec l'attribut android: onClick`, la méthode `showToast ()` doit être `public` et renvoyer` void`. Pour savoir quelle `View` a appelé la méthode, la méthode` showToast () `doit nécessiter un paramètre` view`.

Android Studio fournit un raccourci pour créer un gestionnaire d'événements _stub_ (un espace réservé pour une méthode que vous pourrez renseigner ultérieurement) dans le code de `Activity` associé à la présentation XML. Suivez ces étapes:

1. Dans le fichier de présentation XML (tel que `activity_main.xml`), cliquez sur le nom de la méthode dans l'instruction d'attribut` android: onClick` (`showToast` dans le fragment XML ci-dessus).
2. Appuyez sur**Alt-Enter**sous Windows ou**Option-Return**sous Mac OS X, puis sélectionnez**Créer un gestionnaire d’événements onClick**.
3. Sélectionnez le `Activité` associé au fichier de mise en page (tel que**MainActivity**) et cliquez sur**OK**. Android Studio crée un stub de méthode d'espace réservé dans `MainActivity.java`, comme indiqué ci-dessous.

    public void showToast (Afficher la vue) {
            // Faites quelque chose en réponse au clic du bouton.
    }

### Mise à jour d'une vue

Pour mettre à jour une `View`, par exemple pour remplacer le texte dans une` TextView`, votre code doit d'abord instancier un objet à partir de la `View`. Votre code peut alors mettre à jour l'objet, ce qui met à jour l'écran.

Pour faire référence à la `View` dans votre code, utilisez la méthode [ findViewById () ](https://developer.android.com/reference/android/view/View.html#findViewById (int)) du` La classe View`, qui recherche un `View` basé sur la ressource` id`. Par exemple, l'instruction suivante définit `mShowCount` comme` TextView` dans la présentation avec l'ID de ressource `show_count`:

    mShowCount = (TextView) findViewById (R.id.show_count);

À partir de là, votre code peut utiliser `mShowCount` pour représenter le` TextView`. Ainsi, lorsque vous mettez à jour `mShowCount`, le` TextView` est mis à jour.

Par exemple, lorsque le `Button` suivant avec l'attribut android: onClick` est activé,` onClick` appelle la méthode `countUp ()`:

    android: onClick = "countUp"

Vous pouvez implémenter `countUp ()` pour incrémenter le décompte, convertir le décompte en chaîne et définir la chaîne comme texte pour l'objet `mShowCount`:

    public void countUp (Afficher la vue) {
            mCount ++;
            if (mShowCount! = null)
                mShowCount.setText (Integer.toString (mCount));
    }

Comme vous aviez déjà associé `mShowCount` au` TextView` pour afficher le nombre, la méthode `mShowCount.setText ()` met à jour le `TextView` à l'écran.


### En savoir plus

Documentation d'Android Studio:

* [Guide de l'utilisateur Android Studio](https://developer.android.com/studio/intro/index.html)
* [Image Asset Studio](http://developer.android.com/tools/help/image-asset-studio.html)

Documentation développeur Android:

* [Présentation de l'interface utilisateur](https://developer.android.com/guide/topics/ui/overview.html)
* [Construire une interface utilisateur avec l'éditeur de mise en page](https://developer.android.com/studio/write/layout-editor.html)
* [Construire une interface utilisateur réactive avec ConstraintLayout](https://developer.android.com/training/constraint-layout/index.html)
* [Layouts](http://developer.android.com/guide/topics/ui/declaring-layout.html)
* [View](http://developer.android.com/reference/android/view/View.html)
* [Button](http://developer.android.com/reference/android/widget/Button.html)
* [TextView](http://developer.android.com/reference/android/widget/TextView.html)
* [Événements d'entrée Android](http://developer.android.com/guide/topics/ui/ui-events.html)
* [Contexte](http://developer.android.com/reference/android/content/Context.html)
* [Objets de mise en forme courants](https://developer.android.com/guide/topics/ui/layout-objects.html)
* [Color](https://developer.android.com/reference/android/graphics/Color.html)
* [Ressources Android](http://developer.android.com/guide/topics/resources/index.html)
* [Ressources standard Android R.color](http://developer.android.com/reference/android/R.color.html)
* [Prise en charge de différentes densités](http://developer.android.com/training/multiscreen/screendensities.html)

Conception matérielle:

* [Style](https://material.google.com/style/color.html#)
* [Utilisation du thème Matériau](https://developer.android.com/training/material/theme.html)

Autre:

* Codelabs: [Utilisation de ConstraintLayout pour concevoir vos vues](https://codelabs.developers.google.com/codelabs/constraint-layout/index.html)
* [Visionneuse de hiérarchie](https://developer.android.com/studio/profile/hierarchy-viewer-walkthru.html)
* [Codes de couleur Hex couleur](http://www.color-hex.com/)
* [Glossaire de mots et concepts de vocabulaire](https://developers.google.com/android/for-all/vocab-words/)



## Texte et Vues défilantes (Text, Scrolling views)

**Contenu:**

* [TextView](#textview)
* [Vues défilantes](#scrolling_views)
* [En savoir plus](#learnmore)


Ce chapitre décrit l’une des sous-classes [View] les plus utilisées (https://developer.android.com/reference/android/view/View.html) dans les applications: la [TextView](https://developer.android. com/reference/android/widget/TextView.html), qui affiche le contenu textuel à l'écran.
Un `TextView` peut être utilisé pour afficher un message, une réponse d'une base de données ou même des articles entiers de style magazine que les utilisateurs peuvent faire défiler.

Ce chapitre explique également comment créer une ScrollView et d’autres éléments.

### Affichage

Une sous-classe `View` que vous pouvez souvent utiliser est la classe [TextView](https://developer.android.com/reference/android/widget/TextView.html), qui affiche le texte à l'écran. Vous pouvez utiliser `TextView` pour une` View` de n'importe quelle taille, d'un seul caractère ou mot à un plein écran de texte. Vous pouvez ajouter une ressource `id` à la` TextView` dans la présentation et contrôler l'aspect du texte à l'aide des attributs du fichier de présentation.

Vous pouvez faire référence à un `TextView` dans votre code Java en utilisant sa ressource` id` afin de mettre à jour le texte ou ses attributs à partir de votre code. Si vous souhaitez autoriser les utilisateurs à modifier le texte, utilisez [EditText](https://developer.android.com/reference/android/widget/EditText.html), une sous-classe de `TextView` qui permet la saisie et l'édition de texte.

#### Attributs TextView

Vous pouvez utiliser des attributs XML pour un `TextView` pour contrôler:

* Où le `TextView` est positionné dans une mise en page (comme toute autre vue)
* Comment le `TextView` lui-même apparaît, comme avec une couleur de fond
* A quoi ressemble le texte dans le `TextView`, tel que le texte initial et son style, sa taille et sa couleur

Par exemple, pour définir la largeur, la hauteur et la valeur du texte initial de la vue:

> ``` bash
>  <TextView
>  android: layout_width = "wrap_content"
>  android: layout_height = "wrap_content"
>  android: text = "Bonjour le monde!"
>  <! - plus d'attributs ->
>  />
> ```

Vous pouvez extraire la chaîne de texte dans une ressource chaîne (peut-être appelée `hello_world`) qui est plus facile à gérer pour les versions multilingues de l'application ou si vous devez modifier la chaîne ultérieurement. Après avoir extrait la chaîne, utilisez le nom de la ressource chaîne avec `@ string /` pour spécifier le texte:

> ``` bash
>  <TextView
>  android: layout_width = "wrap_content"
>  android: layout_height = "wrap_content"
>  android: text = "@ string/hello_world"
>  <! - plus d'attributs ->
>  />
> ```

En plus de `android: layout_width` et` android: layout_height` (requis pour un `TextView`), les attributs les plus souvent utilisés avec` TextView` sont les suivants:

* [android: text](https://developer.android.com/reference/android/widget/TextView.html#attr_android:text): définissez le texte à afficher.
* [android: textColor](https://developer.android.com/reference/android/widget/TextView.html#attr_android:textColor): définissez la couleur du texte. Vous pouvez définir l'attribut sur une valeur de couleur, une ressource prédéfinie ou un thème. Les ressources et les thèmes de couleur sont décrits dans d'autres chapitres.
* [android: textAppearance](https://developer.android.com/reference/android/widget/TextView.html#attr_android:textAppearance): apparence du texte, y compris sa couleur, son caractère, son style et sa taille. Vous définissez cet attribut sur une ressource de style prédéfinie ou un thème qui définit déjà ces valeurs.
* [android: textSize](https://developer.android.com/reference/android/widget/TextView.html#attr_android:textSize): définissez la taille du texte (si ce n'est déjà défini par `android: textAppearance`). Utilisez des tailles `sp` (pixels dimensionnés) telles que` 20sp` ou `14.5sp`, ou définissez l'attribut sur une ressource ou un thème prédéfini.
* [android: textStyle](https://developer.android.com/reference/android/widget/TextView.html#attr_android:textStyle): Définissez le style de texte (s'il n'est pas déjà défini par `android: textAppearance`). Utilisez `normal`,` bold`, `italic` ou` bold` | `italic`.
* [android: fontface](https://developer.android.com/reference/android/widget/TextView.html#attr_android:typeface): Définissez la police de texte (si elle n'est pas déjà définie par `android: textAppearance`). Utilisez `normal`,` sans`, `serif` ou` monospace`.
* [android: lineSpacingExtra](https://developer.android.com/reference/android/widget/TextView.html#attr_android:lineSpacingExtra): définissez un espacement supplémentaire entre les lignes de texte. Utilisez des tailles `sp` (pixel redimensionné) ou dp (pixel indépendant du périphérique) ou définissez l'attribut sur une ressource ou un thème prédéfini.
* [android: autoLink](https://developer.android.com/reference/android/widget/TextView.html#attr_android:autoLink): permet de contrôler si des liens tels que des URL et des adresses électroniques sont automatiquement trouvés et convertis en cliquable (touchable). ) liens.

Utilisez l’un des éléments suivants avec `android: autoLink`:

* `none`: ne correspond à aucun motif (par défaut).
* `web`: correspond aux URL Web.
* `email`: correspond aux adresses e-mail.
* `phone`: correspond aux numéros de téléphone.
* `map`: correspond aux adresses de la carte.
* `all`: correspond à tous les modèles (équivalent à Web | email | téléphone | carte).

Par exemple, pour que l'attribut corresponde aux URL Web, utilisez `android: autoLink =" web "`.

#### Utilisation de balises incorporées dans le texte

Dans une application qui accède à des articles de magazines ou de journaux, les articles parus proviendraient probablement d'une source en ligne ou pourraient être enregistrés à l'avance dans une base de données sur l'appareil. Vous pouvez également créer du texte en tant que chaîne longue unique dans la ressource strings.xml.

Dans les deux cas, le texte peut contenir des balises HTML incorporées ou d'autres codes de formatage de texte. Pour s'afficher correctement dans une vue texte, le texte doit être formaté en respectant les règles suivantes:

* Entrez **\ n** pour représenter la fin d'une ligne et un autre **\n** pour représenter une ligne vide. Vous devez ajouter des caractères de fin de ligne pour éviter que les paragraphes ne se superposent.
* Si vous avez une apostrophe (`'`) dans votre texte, vous devez la quitter en la faisant précéder d'une barre oblique inverse (**\'**). Si vous avez une double citation dans votre texte, vous devez également l'échapper (**\ "**). Vous devez également échapper à tout autre caractère non-ASCII. Voir la section" [Formatage et style](https://développeur .android.com/guide/topics/resources/string-resource.html#FormattingAndStyling) "section de String Resources pour plus de détails.
* Entrez les balises HTML et **</ b>** autour des mots qui doivent être en gras.
* Entrez les balises HTML et **</ i>** autour des mots qui doivent être en italique. Notez cependant que si vous utilisez des apostrophes recourbées dans une phrase en italique, vous devez les remplacer par des apostrophes droites.
* Vous pouvez combiner des caractères gras et italiques en combinant les balises, comme dans ****_..._**** mots...**</ i> </ b>**. Les autres balises HTML sont ignorées.
* Pour créer une longue chaîne de texte dans le fichier `strings.xml`, placez le texte entier entre` <string name = "` _votre_nom_string_` "> </ string>` (_votre_nom_string_ est le nom que vous avez fourni à la chaîne de ressources, telle que comme `article_text`).
* Lorsque vous entrez ou collez du texte dans le fichier `strings.xml`, les lignes de texte ne sont pas renvoyées à la ligne suivante, elles s'étendent au-delà de la marge de droite. C'est le comportement correct - chaque nouvelle ligne de texte commençant par la marge de gauche représente un paragraphe entier.

> Positive
> : Si vous souhaitez voir le texte enveloppé dans strings.xml, vous pouvez appuyer sur Retour pour saisir les fins de ligne, ou formater le texte en premier dans un éditeur de texte avec des fins de ligne. Les fins ne seront pas affichées à l'écran.

#### Référerence à un TextView dans le code

Pour faire référence à un `TextView` dans le code, utilisez sa ressource` id`. Par exemple, pour mettre à jour un `TextView` avec un nouveau texte, vous devez:

1. Recherchez le `TextView` et assignez-le à une variable. Vous utilisez la méthode [findViewById ()](https://developer.android.com/reference/android/view/View.html#findViewById (int)) de la classe `View` et vous référez à la vue que vous souhaitez utiliser. trouver en utilisant ce format:

> ``` bash
> R.id.view_id
> ```

Dans lequel _view_id_ est l'identifiant de la ressource pour la vue (tel que `show_count`):

> ``` bash
> mShowCount = (TextView) findViewById (R.id.show_count);
> ```
       

2. Après avoir récupéré `View` en tant que variable membre` TextView`, vous pouvez ensuite définir le texte avec un nouveau texte (dans ce cas, `mCount_text`) à l'aide de [setText ()](https://developer.android. com/reference/android/widget/TextView.html # setText (java.lang.CharSequence)) méthode de la classe `TextView`:

> ``` bash
> mShowCount.setText (mCount_text);
> ```
         

### ScrollView (Vue Défilante)

Si les informations que vous souhaitez afficher dans votre application sont plus grandes que l'affichage de l'appareil, vous pouvez créer une ScrollView que l'utilisateur peut faire défiler verticalement en glissant vers le haut ou le bas, ou horizontalement en faisant glisser le curseur vers la gauche ou vers la droite.

Vous utiliseriez généralement une ScrollView pour les reportages, les articles ou tout texte volumineux qui ne tient pas complètement à l'écran. Vous pouvez également utiliser une ScrollView pour combiner des vues (telles qu'une `TextView` et un` Button`) dans une ScrollView.

#### Création d'une mise en page avec ScrollView

La classe [ScrollView](https://developer.android.com/reference/android/widget/ScrollView.html) fournit la mise en page pour une vue à défilement vertical. (Pour le défilement horizontal, vous utiliseriez [HorizontalScrollView](https://developer.android.com/reference/android/widget/HorizontalScrollView.html).) `ScrollView` est une sous-classe de [FrameLayout](https://developer .android.com/reference/android/widget/FrameLayout.html), ce qui signifie que vous ne pouvez placer que _one_ `View` en tant qu'enfant dans celui-ci; cet enfant contient tout le contenu à faire défiler.

![Une vue de défilement avec une vue enfant](images/dg_scrollview_layout_diagram.png)

Même si vous ne pouvez placer qu’un seul `View` enfant dans une` ScrollView`, celui-ci `View` peut être un [ViewGroup](https://developer.android.com/reference/android/view/ViewGroup.html) avec une hiérarchie d'éléments enfant `View`, telle qu'un [LinearLayout](https://developer.android.com/reference/android/widget/LinearLayout.html). Un bon choix pour un `Voir` dans un` ScrollView` est un `LinearLayout` qui est disposé dans une orientation verticale.

![Une ScrollView avec LinearLayout](images/dg_scrollview_linearlayout_diagram.png)

#### ScrollView et performance

Tout le contenu d'un `ScrollView` (tel qu'un` ViewGroup` avec des éléments `View`) occupe la mémoire et la hiérarchie des vues, même si des parties ne sont pas affichées à l'écran. Cela rend `ScrollView` utile pour faire défiler en douceur les pages de texte de forme libre, car le texte est déjà en mémoire. Cependant, une ScrollView avec un `ViewGroup` avec des éléments` View` peut utiliser beaucoup de mémoire, ce qui peut affecter les performances du reste de votre application.

L'utilisation d'instances imbriquées de `LinearLayout` peut également entraîner une hiérarchie de vues trop profonde, ce qui peut ralentir les performances. L'imbrication de plusieurs instances de `LinearLayout` utilisant l'attribut` android: layout_weight` peut être particulièrement coûteuse car chaque enfant `View` doit être mesuré deux fois. Pensez à utiliser des mises en page plus plates telles que [RelativeLayout](https://developer.android.com/reference/android/widget/RelativeLayout.html) ou [GridLayout](https://developer.android.com/reference/android/widget/ /GridLayout.html) pour améliorer les performances.

Les mises en page complexes avec `ScrollView` peuvent présenter des problèmes de performances, en particulier avec les images. Nous vous recommandons de ne pas utiliser d'images dans un `ScrollView`. Pour afficher de longues listes d'éléments ou d'images, utilisez un [RecyclerView](https://developer.android.com/reference/android/support/v7/widget/RecyclerView.html), traité dans un autre chapitre.

#### ScrollView avec un TextView

Pour afficher un article de magazine déroulant à l'écran, vous pouvez utiliser un [RelativeLayout](https://developer.android.com/reference/android/widget/RelativeLayout.html) comprenant un `TextView` distinct pour l'en-tête de l'article, un autre pour le sous-titre de l'article et un troisième `TextView` pour le texte de l'article qui défile (voir la figure ci-dessous), défini dans un` ScrollView`. La seule partie de l'écran qui défilerait serait le `ScrollView` avec le texte de l'article. ![La mise en page avec une vue de défilement](images/dg_layout_diagram1.png)

#### ScrollView avec un LinearLayout

`ScrollView` ne peut contenir qu'un seul enfant` View`; Cependant, `View` peut être un [ViewGroup](https://developer.android.com/reference/android/view/ViewGroup.html) contenant plusieurs éléments` View`, tels que [LinearLayout](https://developer.android.com/reference/android/widget/LinearLayout.html). Vous pouvez _nest_ un `ViewGroup` tel que` LinearLayout` _ avec_ le `ScrollView`, en faisant ainsi défiler tout ce qui se trouve à l'intérieur de` LinearLayout`.

Par exemple, si vous souhaitez que la sous-rubrique d'un article défile avec celui-ci même s'il s'agit d'éléments `TextView` distincts, ajoutez un` LinearLayout` à la commande `ScrollView` comme un seul enfant` View`, comme illustré dans la figure ci-dessous. , puis déplacez les sous-titres `TextView` et les éléments d’article dans le` LinearLayout`. L'utilisateur fait défiler l'intégralité de `LinearLayout`, qui comprend le sous-titre et l'article. ![Une couche linéaire à l'intérieur de la vue de défilement](images/dg_layout_diagram2.png)

Lors de l'ajout de `LinearLayout` à l'intérieur d'un` ScrollView`, utilisez `match_parent` pour l'attribut` LinearLayout` `android: layout_width` afin de correspondre à la largeur du parent` ScrollView`, et utilisez `wrap_content` pour l''aide` LinearLayout`` : attribut layout_height` pour le rendre suffisamment grand pour en contenir le contenu.

Comme `ScrollView` ne prend en charge que le défilement vertical, vous devez définir l’attribut d’orientation` LinearLayout` sur vertical (`android: orientation =" vertical "`), de sorte que le `LinearLayout` entier défile verticalement. Par exemple, la disposition XML suivante fait défiler le `article`` TextView` avec le `article_subheading`` TextView`:

    <ScrollView
       android:layout_width="wrap_content"
       android:layout_height="wrap_content"
       android:layout_below="@id/article_heading">

       <LinearLayout
          android:layout_width="match_parent"
          android:layout_height="wrap_content"
          android:orientation="vertical">

          <TextView
             android:id="@+id/article_subheading"
             android:layout_width="match_parent"
             android:layout_height="wrap_content"
             android:padding="@dimen/padding_regular"
             android:text="@string/article_subtitle"
             android:textAppearance=
                           "@android:style/TextAppearance.DeviceDefault" />

          <TextView
             android:id="@+id/article"
             android:layout_width="wrap_content"
             android:layout_height="wrap_content"
             android:autoLink="web"
             android:lineSpacingExtra="@dimen/line_spacing"
             android:padding="@dimen/padding_regular"
             android:text="@string/article_text" />
       </LinearLayout>

    </ScrollView>

### En savoir plus

Documentation développeur Android:

* [ScrollView](https://developer.android.com/reference/android/widget/ScrollView.html)
* [LinearLayout](http://developer.android.com/reference/android/widget/LinearLayout.html)
* [RelativeLayout](https://developer.android.com/reference/android/widget/RelativeLayout.html)
* [Voir](http://developer.android.com/reference/android/view/View.html)
* [Button](http://developer.android.com/reference/android/widget/Button.html)
* [TextView](http://developer.android.com/reference/android/widget/TextView.html)
* [Ressources de chaîne](https://developer.android.com/guide/topics/resources/string-resource.html)
* [Disposition relative](https://developer.android.com/guide/topics/ui/layout/relative.html)

**Autre:**

* Blog des développeurs Android: [Linkify your Text!](Http://android-developers.blogspot.com/2008/03/linkify-your-text.html)
* Codepath: [Travailler avec un TextView](https://guides.codepath.com/android/Working-with-the-TextView)


## Activities and intents

**Contenu:**

* [Introduction](#chapterstart)
* [À propos de l'activity](#à propos des activitys)
* [Créer une activity](#créer des activitys)
* [À propos de l'intent](#à propos des intents)
* [Commencer une activity avec une intent explicite](#activity de départ avec une intent explicite)
* [Passant les données d'une activity à une autre](#passesdatabetweenactivities)
* [Récupérer les données d'une activity](#getdatabackfromactivity)
* [Navigation d'activity](#activitynavigation)
* [En savoir plus](#learnmore)

### Introduction

Dans ce chapitre, vous en apprendrez plus sur la classe [`Activity`](https://developer.android.com/reference/android/app/Activity.html), principal élément constitutif de l'interface utilisateur de votre application. Vous apprendrez également à utiliser un [`Intent`](https://developer.android.com/reference/android/content/Intent.html) pour communiquer d'une activity à une autre.


### À propos des activitys

Une _activity_ représente un seul écran dans votre application avec une interface avec laquelle l'utilisateur peut interagir.

Par exemple, une application de messagerie peut comporter une activity affichant une liste de nouveaux courriers électroniques, une autre activity permettant de composer un courrier électronique..etc.

![Votre application peut démarrer une activity dans une autre application](images/activity-start.png)

En règle générale, une «activity» dans une application est spécifiée comme activity «principale», par exemple, «MainActivity». L'utilisateur voit l'activity principale lorsqu'il lance l'application pour la première fois.

Chaque activity peut démarrer d'autres activitys pour effectuer différentes actions.

Chaque fois qu'une nouvelle activity démarre, l'activity précédente est arrêtée, mais le système conserve l'activity dans une pile ("back stack"). Lorsque l'utilisateur a terminé l'activity en cours et appuie sur le bouton Précédent, l'activity est extraite de la pile, détruite et l'activity précédente reprend.

Lorsqu'une activity est arrêtée du fait d'une nouvelle activity, la première activity est notifiée via les méthodes de rappel du cycle de vie de l'activity.

[_activity lifecycle_]](https://developer.android.com/guide/components/activities/activity-lifecycle.html) est l'ensemble des états dans lesquels une «activity» peut se trouver: lorsque l'activity est créée pour la première fois, arrêté ou repris, et quand le système le détruit.

### Créer une activity

Pour implémenter une [`Activity`](https://developer.android.com/reference/android/app/Activity.html) dans votre application, procédez comme suit:

* Créer une classe Java `Activity`.
* Implémenter une interface utilisateur de base pour `Activity` dans un fichier de présentation XML.
* Déclarez la nouvelL'`activity`dans le fichier`AndroidManifest.xml`.

Lorsque vous créez un nouveau projet pour votre application ou ajoutez une nouvelL'`activity`à votre application en choisissant **Fichier>Nouveau> activity**, le modèle effectue automatiquement les étapes répertoriées ci-dessus.


#### Créer l'activity

Lorsque vous créez un nouveau projet dans Android Studio et que vous choisissez l'option **Backwards Compatibility (AppCompat)**,`MainActivity` est, par défaut, une sous-classe de [`AppCompatActivity`](https://developer.android. com/reference/android/support/v7/app/AppCompatActivity.html).

La classe `AppCompatActivity` vous permet d'utiliser les fonctionnalités à jour de l'application Android telles que la barre d'applications et Material Design, tout en permettant à votre application d'être compatible avec les appareils exécutant des versions plus anciennes d'Android.

Voici une sous-classe squelette de **`AppCompatActivity** :


    public class MainActivity extends AppCompatActivity {
       @Override
       protected void onCreate(Bundle savedInstanceState) {
           super.onCreate(savedInstanceState);
           setContentView(R.layout.activity_main);
       }
    }

La première tâche à effectuer dans votre sous-classe`Activity`consiste à implémenter les méthodes de rappel de cycle de vie`Activity`standard (telles que [`onCreate ()`](https://developer.android.com/reference/android/app/Activity .html #onCreate (android.os.Bundle))) pour gérer les changements d'état pour votre`activity`. Ces changements d'état incluent des choses telles que le moment où l'activity est créée, arrêtée, reprise ou détruite. Vous en apprendrez davantage sur le cycle de vie de`Activity`et les rappels de cycle de vie dans un chapitre différent.

Le rappel obligatoire que votre application doit implémenter est la méthode [`onCreate ()`](https://developer.android.com/reference/android/app/Activity.html#onCreate (android.os.Bundle)). Le système appelle cette méthode lorsqu'il crée votre`Activity`, et tous les composants essentiels de votre`Activity`doivent être initialisés ici. Plus important encore, la méthode`onCreate ()`appelle [`setContentView ()`](https://developer.android.com/reference/android/app/Activity.html#setContentView (int)) pour créer la mise en page principale de L'`activity`.

Vous définissez généralement l'interface utilisateur de votre`Activity`dans un ou plusieurs fichiers de présentation XML. Lorsque la méthode`setContentView ()`est appelée avec le chemin d'accès à un fichier de présentation, le système crée toutes les vues initiales à partir de la présentation spécifiée et les ajoute à votre`activity`. Ceci est souvent appelé _inflating_ la mise en page.

Vous voudrez peut-être aussi souvent implémenter la méthode [`onPause ()`](https://developer.android.com/reference/android/app/Activity.html#onPause ()) dans votre`Activity`. Le système appelle cette méthode comme la première indication que l'utilisateur quitte votre`activity`(bien que cela ne signifie pas toujours que l'activity est en cours de destruction). C'est généralement à cet endroit que vous devez valider toutes les modifications qui devraient être conservées au-delà de la session de l'utilisateur en cours (car l'utilisateur risque de ne pas revenir). Vous en apprendrez plus sur`onPause ()`et tous les autres rappels de cycle de vie dans un chapitre ultérieur.

Outre les rappels de cycle de vie, vous pouvez également implémenter des méthodes dans votre`Activity`pour gérer d'autres comportements tels que la saisie utilisateur ou les clics sur les boutons.


#### Implémenter l'interface utilisateur de l'Activity

L'interface utilisateur d'une activity est fournie par une hiérarchie d'éléments`View`, qui contrôle un espace particulier dans la fenêtre d'activity et peut répondre aux interactions de l'utilisateur.

Le moyen le plus courant de définir une interface utilisateur à l'aide d'éléments`View`consiste à utiliser un fichier de présentation XML stocké dans les ressources de votre application. Définir votre mise en page en XML vous permet de conserver la conception de votre interface utilisateur séparément du code source qui définit le comportement de l'activity.

Vous pouvez également créer de nouveaux éléments`View`directement dans votre code d'activity en insérant de nouveaux objets`View`dans un`ViewGroup`, puis en transmettant la racine`ViewGroup`à`setContentView ()`. Une fois que votre mise en page a été gonflée, quelle que soit sa source, vous pouvez ajouter d'autres éléments`View`n'importe où dans la hiérarchie`View`.


#### Déclarer l'activity dans AndroidManifest.xml

Chaque`Activity`de votre application doit être déclarée dans le fichier`AndroidManifest.xml`avec l'élément`<activity>`, dans la section`<application>`. Lorsque vous créez un nouveau projet ou ajoutez une nouvelL'`activity`à votre projet dans Android Studio, le fichier`AndroidManifest.xml`est créé ou mis à jour pour inclure des déclarations de squelette pour chaque`activity`. Voici la déclaration pour`MainActivity`:

    <activity android:name=".MainActivity" >
       <intent-filter>
          <action android:name="android.intent.action.MAIN" />
          <category android:name="android.intent.category.LAUNCHER" />
       </intent-filter>
    </activity>

L'élément `<activity>` inclut un certain nombre d'attributs pour définir les propriétés de`Activity`, tels que son libellé, son icône ou son thème. Le seul attribut requis est`android: name`, qui spécifie le nom de la classe pour L'`activity`(tel que`MainActivity`). Voir la référence de l'élément [`<activity>`](https://developer.android.com/guide/topics/manifest/activity-element.html) pour plus d'informations sur les déclarations`Activity`.

L'élément `<activity>` peut également inclure des déclarations pour les filtres `Intent`. Les filtres `Intent` spécifient le type d'intent que votre`activity`acceptera.

    <intent-filter>
       <action android:name="android.intent.action.MAIN" />
       <category android:name="android.intent.category.LAUNCHER" />
    </intent-filter>

Les filtres `Intent` doivent inclure au moins un élément`<action>`, et peuvent également inclure une `<category>` et des données facultatives`<data>`.

La`MainActivity`de votre application nécessite un filtre `Intent` qui définit l’action "main" (principale) et la catégorie "launcher" (lanceur) afin que le système puisse lancer votre application.

L'élément `<action>` spécifie qu'il s'agit du point d'entrée "main" de l'application.
L'élément`<category>`spécifie que cette`Activity`doit être listée dans le lanceur d'applications du système (pour permettre aux utilisateurs de lancer cette`Activity`).

Chaque`activity` de votre application peut également déclarer des filtres`Intent`, mais seule votre `MainActivity` doit inclure l'action "main ".

#### Ajouter une autre Activity à votre projet

La `MainActivity` de votre application et son fichier de mise en page associé sont fournis par un modèle `Activity` dans Android Studio, tel que activity vide ou activity de base.

Vous pouvez ajouter une nouvelL'`activity`à votre projet en choisissant **Fichier>Nouveau>activity**.
Choisissez le modèle `Activity` que vous souhaitez utiliser ou ouvrez la galerie pour voir tous les modèles disponibles.

![Galerie d'activity dans Android Studio](images/activity-gallery.png)

Android Studio fournit trois éléments pour chaque nouvelle activity de votre application:

* Un fichier Java pour la nouvelL'`activity`avec une définition de classe et une méthode`onCreate ()`. La nouvelL'`activity`, comme `MainActivity`, est une sous-classe de`AppCompatActivity`.
* Un fichier XML contenant la mise en page de la nouvelle activity (**layout**).
* Un élément `<activity>` supplémentaire dans le fichier`AndroidManifest.xml`qui spécifie la nouvelle activity.

### À propos des Intents

Chaque activity est démarrée ou activée avec un [`Intent`](https://developer.android.com/reference/android/content/Intent.html), qui est un objet de message qui demande au moteur d'exécution Android de démarrer une activity ou un autre composant d'application dans votre application ou dans une autre application.

Lorsque votre application est lancée pour la première fois à partir de l'écran d'accueil de l'appareil, le moteur d'exécution Android envoie un "Intent" à votre application pour démarrer l'activity principale de votre application (celle définie avec l'action MAIN et la catégorie LAUNCHER dans le fichier`AndroidManifest.xml`).

Pour démarrer une autre activity dans votre application ou demander à une autre activity disponible sur le périphérique d'effectuer une action, vous créez votre propre intent et appelez la méthode **`startActivity()`** pour envoyer l'intent.

En plus de démarrer une activity, une intent peut également être utilisée pour **transmettre des données** d'une activity à une autre.


#### Types d'Intent

Les intents peuvent être **_explicite_** ou **_implicite_**:

* **_intent explicite:_** Vous spécifiez l'activity réceptrice (ou un autre composant) à l'aide du nom de classe complet de l'activity. Vous utilisez des intents explicites pour démarrer des composants dans votre propre application (par exemple, pour vous déplacer entre les écrans de l'interface utilisateur), car vous connaissez déjà le package et le nom de la classe de ce composant.

* **_intent implicite:_** Vous ne spécifiez pas une activity spécifique ou un autre composant pour recevoir l'intent. Au lieu de cela, vous déclarez une action générale à effectuer et le système Android associe votre demande à une activity ou à un autre composant capable de gérer l'action demandée. Vous en apprendrez davantage sur l’utilisation d’intents implicites dans une autre pratique.

#### Objets et paramètres d'Intent

Pour un «intent» explicite, les paramètres sont les suivants:

* `Activity` _class_ (pour un`Intent`explicite). Il s’agit du nom de classe de `Activity` ou de tout autre composant devant recevoir l’intent;
* `Intent` _data._ Le champ data `Intent` contient une référence aux données sur lesquelles vous voulez que la `Activity` réceptrice agisse comme un objet Uri.
* `Intent`_ _extras._ Ce sont des paires **clé-valeur** qui transportent les informations nécessaires à`l'activity`qui les reçoit pour accomplir l'action demandée.
* `Intent`[_flags_](https://developer.android.com/reference/android/content/Intent.html#setFlags (int)). Il s'agit de bits supplémentaires de métadonnées, définis par la classe`Intent`. Les drapeaux peuvent indiquer au système Android comment lancer une "activity" ou comment la traiter après son lancement.

Pour un `Intent` implicite, vous devrez peut-être également définir l'action et la catégorie `Intent`.

### Commencer une activity avec un intent explicite

Pour démarrer une `Activity` spécifique à partir d'une autre`Activity`, utilisez un `Intent` explicite et le [`startActivity ()`](https://developer.android.com/reference/android/app/Activity.html#startActivity).

Un `Intent` explicite inclut le nom complet de la classe pour l'`Activity` ou un autre composant de l'objet `Intent`.
Tous les autres paramètres `Intent` sont facultatifs et `null` par défaut.

Example : démarrer `ShowMessageActivity` pour afficher un message spécifique dans une application de messagerie :

    Intent messageIntent = new Intent(this, ShowMessageActivity.class);
    startActivity(messageIntent);

Le constructeur d'intent prend deux arguments (paramètres) pour un `Intent` explicite:

* Un contexte d'application. Dans cet exemple, la classe `Activity` fournit le contexte (`this`).
* Le composant spécifique à démarrer (`ShowMessageActivity.class`).

Utilisez la méthode `startActivity ()` avec le nouvel objet `Intent` comme seul argument.
La méthode `startActivity()` envoie le `Intent` au système Android, qui lance la classe `ShowMessageActivity` au nom de votre application.
La nouvelle `Activity` apparaît à l'écran et l'`Activity` d'origine est mise en pause.

L'`activity` démarrée reste à l'écran jusqu'à ce que l'utilisateur appuie sur le bouton Précédent de l'appareil. À ce moment, cette activity se ferme et est récupérée par le système, et L'`activity`d'origine est reprise.

Vous pouvez également fermer manuellement l'`activity` démarré en réponse à une action de l'utilisateur (comme un clic sur un bouton) avec la méthode [`finish ()`](https://developer.android.com/reference/android/app /Activity.html#finish ()) :

    public void closeActivity (View view) {
        finish();
    }


### Passer des données d'une activity à une autre

En plus de simplement démarrer une `Activity` à partir d'une autre `Activity`, vous utilisez également un `Intent` pour passer des informations_ d'une`Activity` à une autre. L'objet `Intent` que vous utilisez pour démarrer une `Activity` peut inclure`Intent`_data_ (l'URI d'un objet sur lequel agir), ou `Intent` _extras_, qui sont des bits de données supplémentaires dont `Activity` pourrait avoir besoin.

Dans la premiere `Activity`(envoi), vous:

1. Créez l'objet `Intent`.
2. Mettez des données ou des extras dans cette "intent".
3. Lancez la nouvelle `activity` avec `startActivity()`.

Dans la seconde `Activity` (réception), vous:

1. Obtenez l'objet `Intent` avec lequel `Activity` a été démarré.
2. Récupérez les données ou les extras de l'objet `Intent`.


#### Quand utiliser les données d'intent ou les extras d'intent

Vous pouvez utiliser les données`Intent`ou les suppléments`Intent`pour transmettre des données d’une`activity`à une autre. Il existe plusieurs différences essentielles entre les données et les extras qui déterminent celles que vous devez utiliser.

`Intent`_data_ ne peut contenir qu'une seule information: un URI représentant l'emplacement des données sur lesquelles vous souhaitez opérer. Cet URI peut être une URL de page Web (`http://`), un numéro de téléphone (`tel://`), un emplacement géographique (`geo://`) ou tout autre URI personnalisé que vous définissez.

Utilisez le champ de données`Intent`:

* Lorsque vous ne possédez qu'une information, vous devez l'envoyer à L'`activity`démarrée.
* Lorsque cette information est un emplacement de données pouvant être représenté par un URI.

L'intent _extras_ concerne toutes les autres données arbitraires que vous souhaitez transmettre à L'`activity`démarrée. Les extras`Intent`sont stockés dans un objet [`Bundle`](https://developer.android.com/reference/android/os/Bundle.html) en tant que paires clé/valeur. Un`Bundle`est une carte, optimisée pour Android, dans laquelle une clé est une chaîne et une valeur peut être tout type de primitive ou d'objet (les objets doivent implémenter le [`Parcelable`]](https://developer.android.com /reference/android/os/Parcelable.html)). Pour insérer des données dans les extras`Intent`, vous pouvez utiliser l’une des méthodes [`Intent`](https://developer.android.com/reference/android/content/Intent.html) de la classe`putExtra ()`, ou créez votre propre`Bundle`et mettez-le dans le`Intent`avec [`putExtras ()`](https://developer.android.com/reference/android/content/Intent.html#putExtras (android.os.Bundle )).

Utilisez les suppléments `Intent`:

* Si vous souhaitez transmettre plusieurs informations à L'`activity`démarrée.
* Si l’une des informations que vous souhaitez transmettre n’est pas exprimable par un URI.

Les données et les extras`Intent`ne sont pas exclusifs; vous pouvez utiliser des données pour un URI et des extras pour toute information supplémentaire dont a besoin L'`activity`démarrée pour traiter les données dans cet URI.


#### Ajouter des données à l'intent

Pour ajouter des données à un`Intent`explicite à partir de`Activity`d'origine, créez l'objet`Intent`comme vous l'avez fait auparavant:

    intent messageIntent = new Intent (this, ShowMessageActivity.class);

Utilisez la méthode [`setData ()`](https://developer.android.com/reference/android/content/Intent.html#setData (android.net.Uri)) avec un objet Uri pour ajouter cet URI au`intent`. Quelques exemples d'utilisation de`setData ()`avec des URI:

    // A web page URL
    messageIntent.setData(Uri.parse("http://www.google.com"));
    // a Sample file URI
    messageIntent.setData(Uri.fromFile(new File("/sdcard/sample.jpg")));
    // A sample content: URI for your app's data model
    messageIntent.setData(Uri.parse("content://mysample.provider/data"));
    // Custom URI
    messageIntent.setData(Uri.parse("custom:" + dataID + buttonId));

N'oubliez pas que le champ de données ne peut contenir qu'un seul URI; Si vous appelez`setData ()`plusieurs fois, seule la dernière valeur est utilisée. Utilisez les options`Intent`pour inclure des informations supplémentaires (y compris les URI).

Après avoir ajouté les données, vous pouvez démarrer l’activity avec l’intent comme d’habitude:

    startActivity(messageIntent);


#### Ajouter des extras à l'intent

Pour ajouter des options`Intent`à un`Intent`explicite à partir de`Activity`d'origine:

1. Déterminez les clés à utiliser pour les informations que vous souhaitez insérer dans les suppléments ou définissez les vôtres. Chaque information a besoin de sa propre clé.
2. Utilisez les méthodes`putExtra ()`pour ajouter vos paires clé/valeur aux extras de`Intent`. Vous pouvez éventuellement créer un objet [`Bundle`](https://developer.android.com/reference/android/os/Bundle.html), ajouter vos données dans le`Bundle`, puis ajouter le`Bundle`à le`intent`.

La classe [`Intent`](https://developer.android.com/reference/android/content/Intent.html) inclut des clés supplémentaires que vous pouvez utiliser, définies comme des constantes commençant par le mot`EXTRA_`. Par exemple, vous pouvez utiliser [`Intent.EXTRA_EMAIL`](https://developer.android.com/reference/android/content/Intent.html#EXTRA_EMAIL) pour indiquer un tableau d'adresses e-mail (sous forme de chaînes) ou [`Intent.EXTRA_REFERRER`](https://developer.android.com/reference/android/content/Intent.html#EXTRA_REFERRER) pour spécifier des informations sur l '`activity`d'origine qui a envoyé le`Intent`.

Vous pouvez également définir vos propres clés supplémentaires`Intent`. Classiquement, vous définissez les clés supplémentaires`Intent`comme des variables statiques dont le nom commence par EXTRA_. Pour garantir que la clé est unique, la valeur de chaîne pour la clé elle-même doit être précédée du nom de classe complet de votre application. Par exemple:

    public final static String EXTRA_MESSAGE =
                                            "com.example.mysampleapp.MESSAGE";
    public final static String EXTRA_POSITION_X = "com.example.mysampleapp.X";
    public final static String EXTRA_POSITION_Y = "com.example.mysampleapp.Y";

Créez un objet`Intent`(s'il n'en existe pas déjà un):

    Intent messageIntent = new Intent(this, ShowMessageActivity.class);

Utilisez une méthode`putExtra ()`avec une clé pour insérer des données dans les extras de`Intent`. La classe`Intent`définit de nombreuses méthodes`putExtra ()`pour différents types de données:

    messageIntent.putExtra(EXTRA_MESSAGE, "this is my message");
    messageIntent.putExtra(EXTRA_POSITION_X, 100);
    messageIntent.putExtra(EXTRA_POSITION_Y, 500);

Alternativement, vous pouvez créer un nouveau`Bundle`et remplir ce`Bundle`avec vos extras de`Intent`. [`Bundle`](https://developer.android.com/reference/android/os/Bundle.html) définit de nombreuses méthodes de" vente "pour différents types de données primitives ainsi que des objets qui implémentent le [`Parcelable`] d'Android (https://developer.android.com/reference/android/os/Parcelable.html) ou interface [Java] de``Serializable`](https://developer.android.com/reference/java/io/Serializable.html) .


    Bundle extras = new Bundle();
    extras.putString(EXTRA_MESSAGE, "this is my message");
    extras.putInt(EXTRA_POSITION_X, 100);
    extras.putInt(EXTRA_POSITION_Y, 500);

Une fois que vous avez rempli le`Bundle`, ajoutez-le à l’intent avec le [`putExtras ()`](https://developer.android.com/reference/android/content/Intent.html#putExtras (android Méthode .os.Bundle)) (notez le "s" dans`Extras`):

    messageIntent.putExtras(extras);

Commencez l’activity avec l’intent comme d’habitude:

    startActivity(messageIntent);


#### Récupérer les données de l'intent dans l'activity démarrée

Lorsque vous démarrez une`Activity `avec un `Intent`, l'`Activity` démarrée a accès à l'`Intent` et aux données qu'il contient.

Pour récupérer l’intent avec laquelle l’activity a démarré, utilisez le [`getIntent ()`](https://developer.android.com/reference/android/app/Activity.html#getIntent ()) méthode:

    Intent intent = getIntent();

Utilisez [`getData ()`](https://developer.android.com/reference/android/content/Intent.html#getData ()) pour obtenir l'URI de cet`Intent`:

    Uri locationUri = intent.getData();

Pour obtenir les extras de l’intent, vous devez connaître les clés des paires clé/valeur. Vous pouvez utiliser les extras standard`Intent`si vous les avez utilisés, ou vous pouvez utiliser les clés que vous avez définies dans L'`activity`d'origine (si elles ont été définies comme publiques.)

Utilisez l’une des méthodes`getExtra ()`pour extraire des données supplémentaires de l’objet`Intent`:

    String message = intent.getStringExtra(MainActivity.EXTRA_MESSAGE);
    int positionX = intent.getIntExtra(MainActivity.EXTRA_POSITION_X);
    int positionY = intent.getIntExtra(MainActivity.EXTRA_POSITION_Y);

Ou vous pouvez obtenir les extras complets`Bundle`à partir de`Intent`et extraire les valeurs avec les différentes méthodes [`Bundle`](https://developer.android.com/reference/android/os/Bundle.html):

    Bundle extras = intent.getExtras();
    String message = extras.getString(MainActivity.EXTRA_MESSAGE);


### Récupérer les données d'une activity

Lorsque vous démarrez une`Activity`avec un`Intent`, L'`activity`d'origine est suspendue et la nouvelL'`activity`reste à l'écran jusqu'à ce que l'utilisateur clique sur le bouton Précédent ou que vous appeliez la méthode`finish ()`un gestionnaire de clic ou une autre fonction qui met fin à la participation de l'utilisateur avec cette`activity`.

Parfois, lorsque vous envoyez des données à une`Activity`avec un`Intent`, vous souhaitez également récupérer les données de cet`Intent`. Par exemple, vous pouvez démarrer une galerie de photos`activity`qui permet à l’utilisateur de choisir une photo. Dans ce cas, votre`activity`originale doit recevoir des informations sur la photo que l'utilisateur a choisie à partir de L'`activity`lancée.

Pour lancer une nouvelL'`activity`et obtenir un résultat, procédez comme suit dans votre`Activity`d'origine:

1. Au lieu de lancer`Activity`avec`startActivity ()`, appelez [`startActivityForResult ()`](https://developer.android.com/reference/android/app/Activity.html#startActivityForResult (android.content .Intent,% 20int)) avec l’intent et un code de requête.
2. Créez une nouvelle "intent" dans la "activity" lancée et ajoutez les données de retour à cette "intent".
3. Implémentez`onActivityResult ()`dans`Activity`d'origine pour traiter les données renvoyées.

Vous en apprendrez plus sur chacune de ces étapes dans les sections suivantes.


#### Utiliser startActivityForResult () pour lancer l'activity.

Pour récupérer les données d'une`Activity`lancée, démarrez-la avec le [`startActivityForResult ()`](https://developer.android.com/reference/android/app/Activity.html#startActivityForResult (android. content.Intent,% 20int)) méthode au lieu de`startActivity ()`.

    startActivityForResult(messageIntent, TEXT_REQUEST);

La méthode`startActivityForResult ()`, comme`startActivity ()`, prend un argument`Intent`qui contient des informations sur L'`activity`à lancer et toutes les données à envoyer à cette`Activity`. La méthode`startActivityForResult ()`, cependant, a également besoin d'un code de requête.

Le code de demande est un entier qui identifie la demande et peut être utilisé pour différencier les résultats lorsque vous traitez les données renvoyées. Par exemple, si vous lancez une`activity`pour prendre une photo et une autre pour choisir une photo dans une galerie, vous avez besoin de codes de demande différents pour identifier la demande à laquelle les données renvoyées appartiennent.

Classiquement, vous définissez les codes de demande sous forme de variables entières statiques dont les noms incluent`REQUEST`. Utilisez un entier différent pour chaque code. Par exemple:

    public static final int PHOTO_REQUEST = 1;
    public static final int PHOTO_PICK_REQUEST = 2;
    public static final int TEXT_REQUEST = 3;


#### Renvoyer une réponse de l'Activity lancée

Les données de réponse du`Activity`lancé au`Activity`d'origine sont envoyées dans un`Intent`, soit dans les données, soit dans les extras. Vous construisez ce retour`Intent`et y insérez les données de la même manière que pour l'envoi`Intent`. En règle générale, votre`activity`lancée aura une méthode de rappel`onClick ()`ou une autre entrée utilisateur dans laquelle vous traitez l'action de l'utilisateur et fermez L'`activity`. C'est également à cet endroit que vous construisez la réponse.

Pour renvoyer des données à partir de`Activity`lancé, créez un nouvel objet`Intent`vide.

    Intent returnIntent = new Intent();

**Remarque:** Pour éviter de confondre les données envoyées avec les données renvoyées, utilisez un nouvel objet`Intent`plutôt que de réutiliser l'objet`Intent`d'envoi d'origine.

Un résultat de retour`Intent`n'a pas besoin d'un nom de classe ou de composant pour se retrouver au bon endroit. Le système Android renvoie la réponse à L'`activity`d'origine pour vous.

Ajoutez des données ou des extras à l’intent de la même manière que vous l’avez fait avec l’intent initiale. Vous devrez peut-être définir des clés pour les extras de retour`Intent`au début de votre classe.

    public final static String EXTRA_RETURN_MESSAGE =
                                      "com.example.mysampleapp.RETURN_MESSAGE";

Puis mettez vos données de retour dans le`Intent`comme d'habitude. Dans ce qui suit, le message de retour est un "Intent" supplémentaire avec la clé`EXTRA_RETURN_MESSAGE`.

    messageIntent.putExtra(EXTRA_RETURN_MESSAGE, mMessage);

Utilisez la méthode`setResult ()`avec un code de réponse et le`Intent`avec les données de réponse:

    setResult(RESULT_OK,replyIntent);

Les codes de réponse sont définis par la classe [`Activity`](https://developer.android.com/reference/android/app/Activity.html) et peuvent être

*`RESULT_OK`: la requête a abouti.
*`RESULT_CANCELED`: l'utilisateur a annulé l'opération.
*`RESULT_FIRST_USER`: Pour définir vos propres codes de résultat.

Vous utilisez le code de résultat dans L'`activity`d'origine.

Enfin, appelez`finish ()`pour fermer L'`activity`et reprendre L'`activity`d'origine:

    finish();

#### Lire les données de réponse dans onActivityResult()

Maintenant que`Activity`lancé a renvoyé les données à`Activity`d'origine avec un`Intent`, cette première`Activity`doit gérer ces données. Pour gérer les données renvoyées dans`Activity`d'origine, implémentez la méthode de rappel`onActivityResult ()`. Voici un exemple simple.

    public void onActivityResult(int requestCode, int resultCode,  Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        if (requestCode == TEXT_REQUEST) {
            if (resultCode == RESULT_OK) {
                String reply =
                   data.getStringExtra(SecondActivity.EXTRA_RETURN_MESSAGE);
                   // process data
            }
        }
    }

Les trois arguments de`onActivityResult ()`contiennent toutes les informations nécessaires pour gérer les données de retour.

* _ Code de demande: _ Le code de requête que vous avez défini lors du lancement de`Activity`avec`startActivityForResult ()`. Si vous lancez une`activity`différente pour effectuer différentes opérations, utilisez ce code pour identifier les données spécifiques que vous récupérez.
* _Result code: _ le code de résultat défini dans l '`activity`lancée, généralement l'un des éléments`RESULT_OK`ou`RESULT_CANCELED`.
* _Intent data: _ the`Intent`qui contient les données renvoyées par le lancement`Activity`.

L'exemple de méthode présenté ci-dessus montre la logique typique de traitement des codes de demande et de réponse. Le premier test concerne la demande`TEXT_REQUEST`et que le résultat a abouti. À l'intérieur du corps de ces tests, vous extrayez les informations de retour de l'intent. Utilisez`getData ()`pour obtenir les données`Intent`ou`getExtra ()`pour extraire des valeurs des extras`Intent`avec une clé spécifique.


### Navigation dans les Activitys

Toute application de la complexité que vous construisez inclura plus d'une`activity`. Au fur et à mesure que vos utilisateurs se déplacent dans votre application et d'une activity à une autre, une navigation cohérente devient de plus en plus importante pour l'expérience utilisateur de l'application. Peu de choses frustrent davantage les utilisateurs que la navigation de base qui se comporte de manière incohérente et inattendue. Une conception réfléchie de la navigation de votre application rendra l’utilisation de votre application prévisible et fiable pour vos utilisateurs.

Le système Android prend en charge deux formes différentes de stratégies de navigation pour votre application.

* Navigation (temporelle) fournie par le bouton Précédent de l'appareil et la pile arrière.
* Navigation vers le haut (ancestrale), fournie par vous en option dans la barre des applications.


#### Navigation arrière, tâches et pile arrière

La navigation arrière permet à vos utilisateurs de revenir à la précédente`activity`en appuyant sur le bouton de retour du périphérique
![Bouton de retour du périphérique](images/ic_back-button.png).
La navigation arrière est également appelée navigation _temporelle_ car le bouton Précédent permet de parcourir l'historique des écrans récemment visionnés, dans l'ordre chronologique inverse.

Le _back stack_ est l'ensemble de chaque`Activity`que l'utilisateur a visité et sur lequel l'utilisateur peut retourner à l'aide du bouton de retour. Chaque fois qu'une nouvelL'`activity`commence, elle est poussée dans la pile arrière et prend le focus de l'utilisateur. La précédente`Activity`est arrêtée mais reste disponible dans la pile arrière. La pile arrière fonctionne sur un mécanisme "dernier entré, premier sorti". Ainsi, lorsque l'utilisateur en a terminé avec l'actuelle "activity" et appuie sur le bouton Précédent, cette "activity" est extraite de la pile (et détruite) et la précédente`L'activity reprend.

Because an app can start an`Activity`both inside and outside a single app, the back stack contains each`Activity`that has been launched by the user in reverse order. Each time the user presses the Back button, each`Activity`in the stack is popped off to reveal the previous one, until the user returns to the Home screen. ![The Activity back stack](images/diagram_backstack.png)

Android fournit une pile arrière pour chaque tâche. Une tâche est un concept d'organisation pour chaque`activity`avec laquelle l'utilisateur interagit lors de l'exécution d'une opération, que celle-ci se trouve dans votre application ou dans plusieurs applications. La plupart des tâches démarrent à partir de l'écran d'accueil Android et le fait de toucher une icône d'application lance une tâche (et une nouvelle pile arrière) pour cette application. Si l'utilisateur utilise une application pendant un certain temps, appuie sur la touche d'accueil et démarre une nouvelle application, cette nouvelle application se lance dans sa propre tâche et possède sa propre pile d'arrière-plan. Si l'utilisateur revient à la première application, la pile arrière de cette première tâche est renvoyée. En naviguant avec le bouton Précédent, vous revenez uniquement à`Activity`dans la tâche en cours, pas à toutes les tâches exécutées sur le périphérique. Android permet à l'utilisateur de naviguer entre les tâches à l'aide de l'écran de synthèse ou des tâches récentes, accessible via le bouton carré situé dans le coin inférieur droit de l'appareil
![Bouton de tâche du périphérique](images/ic_task-button.png).
![Ecran Tâches récentes](images/overview-screen.png)

Dans la plupart des cas, vous n'avez pas à vous préoccuper de la gestion des tâches ni de la pile arrière de votre application: le système en assure le suivi pour vous et le bouton Précédent est toujours disponible sur l'appareil.

Il peut toutefois arriver que vous souhaitiez parfois remplacer le comportement par défaut pour les tâches ou pour la pile arrière. Par exemple, si votre écran contient un navigateur Web intégré dans lequel les utilisateurs peuvent naviguer entre les pages Web, vous pouvez utiliser le comportement par défaut du navigateur lorsque les utilisateurs appuient sur le bouton _Retour_ du périphérique, plutôt que de revenir à L'`activity`précédente. Vous devrez peut-être également modifier le comportement par défaut de votre application dans d'autres cas particuliers, tels que les notifications ou les widgets, dans lesquels une «activity» au sein de votre application peut être lancée en tant que tâche propre, sans pile arrière. Vous en apprendrez plus sur la gestion des tâches et la pile arrière dans une section ultérieure.

#### Navigation vers le haut

La navigation vers le haut, parfois appelée navigation ancestrale ou logique, permet de naviguer dans une application en fonction des relations hiérarchiques explicites entre les écrans. Avec la navigation vers le haut, chaque "activity" est organisée dans une hiérarchie et chaque "enfant" indique une flèche orientée vers la gauche dans la barre des applications![Bouton Haut (dans la barre des applications)](images/ic_up-button.png ) qui renvoie l'utilisateur au "parent"`Activity`. La plus haute`Activity`dans la hiérarchie est généralement`MainActivity`, et l'utilisateur ne peut pas monter à partir de là.
![Bouton de navigation vers le haut](images/up_navigation_in_app_bar_cropped.png)

Par exemple, si l’activity principale dans une application de messagerie est une liste de tous les messages, la sélection d’un message lance une seconde activity pour afficher cet e-mail unique. Dans ce cas, le message ʻactivity`fournira un bouton Haut qui permet de revenir à la liste des messages.

Le comportement du bouton Haut est défini par vous dans chaque`activity`en fonction de la conception de la navigation de votre application. Dans de nombreux cas, la navigation vers le haut et vers le bas peut donner le même comportement: revenir simplement à L'`activity`précédente. Par exemple, une "activity" de paramètres peut être disponible à partir de n'importe quelle "activity" de votre application. "Up" est donc identique à l'arrière - il suffit de ramener l'utilisateur à sa place précédente dans la hiérarchie.

Fournir un comportement vers le haut pour votre application est facultatif, mais constitue une bonne pratique de conception afin de permettre une navigation cohérente pour votre application.


#### Implémenter la navigation vers le haut avec une Activity parent

Avec les projets de modèles standard dans Android Studio, il est simple d'implémenter la navigation vers le haut. Si une`Activity`est l'enfant d'une autre`Activity`dans la hiérarchie`Activity`de votre application, spécifiez le parent de cet autre`Activity`dans le fichier`AndroidManifest.xml`.

À partir d'Android 4.1 (niveau 16 de l'API), déclarez le parent logique de chaque`Activity`en spécifiant l'attribut`android: parentActivityName`dans l'élément`<activity>`. Pour prendre en charge les anciennes versions d'Android, incluez des informations`<méta-données>`pour définir explicitement L'`activity`parent. Utilisez les deux méthodes pour être rétro-compatible avec toutes les versions d'Android.

Voici les définitions du squelette dans`AndroidManifest.xml`pour une`Activity`(parent) principale (parent) et une deuxième (enfant)`Activity`(`SecondActivity`):


    <application
        android:allowBackup="true"
        android:icon="@mipmap/ic_launcher"
        android:label="@string/app_name"
        android:roundIcon="@mipmap/ic_launcher_round"
        android:supportsRtl="true"
        android:theme="@style/AppTheme">
        <!-- The main activity (it has no parent activity) -->
        <activity android:name=".MainActivity">
           <intent-filter>
                <action android:name="android.intent.action.MAIN" />

                <category android:name="android.intent.category.LAUNCHER" />
           </intent-filter>
        </activity>
        <!-- The child activity) -->
        <activity android:name=".SecondActivity"
           android:label = "Second Activity"
           android:parentActivityName=".MainActivity">
           <meta-data
              android:name="android.support.PARENT_ACTIVITY"
              android:value="com.example.android.twoactivities.MainActivity" />
           </activity>
    </application>



### En savoir plus

Android developer documentation:

*   [Application Fundamentals](http://developer.android.com/guide/components/fundamentals.html)
*   [Activities](http://developer.android.com/guide/components/activities.html)
*   [Intents and Intent Filters](http://developer.android.com/guide/components/intents-filters.html)
*   [Designing Back and Up navigation](https://developer.android.com/training/design-navigation/ancestral-temporal)
*   [Activity](http://developer.android.com/reference/android/app/Activity.html)
*   [Intent](http://developer.android.com/reference/android/content/Intent.html)
*   [ScrollView](https://developer.android.com/reference/android/widget/ScrollView.html)
*   [View](http://developer.android.com/reference/android/view/View.html)
