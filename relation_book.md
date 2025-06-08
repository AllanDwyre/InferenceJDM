# Cheat sheet des relations de JDM :
* **r_associated** (idée associée) ^0^:
	➤ Définition :	*Il est demandé d'énumérer les termes les plus étroitement associés au mot cible... Ce mot vous fait penser à quoi ?*
	➤ Inverse :	*r_associated*

* **r_raff_sem** (raffinement sémantique) ^1^:
	➤ Définition :	*Raffinement sémantique vers un usage particulier du terme source*
	➤ Inverse :	*r_raff_sem-1*

* **r_raff_morpho** (raffinement morphologique) ^2^:
	➤ Définition :	*Raffinement morphologique vers un usage particulier du terme source*

* **r_domain** (domaine) ^3^:
	➤ Définition :	*Il est demandé de fournir des domaines relatifs au mot cible. *
	➤ Example :	*pour 'corner', on pourra donner les domaines 'football' ou 'sport'.*
	➤ Inverse :	*r_domain-1*

* **r_pos** (POS) ^4^:
	➤ Définition :	*Partie du discours (Nom, Verbe, Adjectif, Adverbe, etc.)*

* **r_syn** (synonyme) ^5^:
	➤ Définition :	*Il est demandé d'énumérer les synonymes ou quasi-synonymes de ce terme.*
	➤ Inverse :	*r_syn*

* **r_isa** (générique) ^6^:
	➤ Définition :	*Il est demandé d'énumérer les GENERIQUES/hyperonymes du terme. *
	➤ Example :	*'animal' et 'mammifère' sont des génériques de 'chat'.*
	➤ Inverse :	*r_hypo*

* **r_anto** (contraire) ^7^:
	➤ Définition :	*Il est demandé d'énumérer des contraires du terme. *
	➤ Example :	*'chaud' est le contraire de 'froid'.*

* **r_hypo** (spécifique) ^8^:
	➤ Définition :	*Il est demandé d'énumérer des SPECIFIQUES/hyponymes du terme. *
	➤ Example :	*'mouche', 'abeille', 'guêpe' pour 'insecte'.*
	➤ Inverse :	*r_isa*

* **r_has_part** (partie) ^9^:
	➤ Définition :	*Il faut donner des PARTIES/constituants/éléments (a pour méronymes) du mot cible. *
	➤ Example :	*'voiture' a comme parties : 'porte', 'roue', 'moteur', ...*
	➤ Inverse :	*r_holo*

* **r_holo** (tout) ^10^:
	➤ Définition :	*Il est démandé d'énumérer des 'TOUT' (a pour holonymes)  de l'objet en question. Pour 'main', on aura 'bras', 'corps', 'personne', etc... Le tout est aussi l'ensemble comme 'classe' pour 'élève'.*
	➤ Inverse :	*r_has_part*

* **r_locution** (locution) ^11^:
	➤ Définition :	*A partir d'un terme, il est demandé d'énumérer les locutions, expression ou mots composés en rapport avec ce terme. *
	➤ Example :	*pour 'moulin', ou pourra avoir 'moulin à vent', 'moulin à eau', 'moulin à café'. Pour 'vendre', on pourra avoir 'vendre la peau de l'ours avant de l'avoir tué', 'vendre à perte', etc..*

* **r_agent** (action>agent) ^13^:
	➤ Définition :	*L'agent (qu'on appelle aussi le sujet) est l'entité qui effectue l'action, OU la subit pour des formes passives ou des verbes d'état. *
	➤ Example :	*dans - Le chat mange la souris -, l'agent est le chat. Des agents typiques de 'courir' peuvent être 'sportif', 'enfant',... (manger r_agent chat)*
	➤ Inverse :	*r_agent-1*

* **r_patient** (action>patient) ^14^:
	➤ Définition :	*Le patient (qu'on appelle aussi l'objet) est l'entité qui subit l'action. Par exemple dans - Le chat mange la souris -, le patient est la souris. Des patients typiques de manger peuvent être 'viande', 'légume', 'pain', ... (manger r_patient pain)*
	➤ Inverse :	*r_patient-1*

* **r_lieu** (chose>lieu) ^15^:
	➤ Définition :	*Il est demandé d'énumérer les LIEUX typiques où peut se trouver le terme/objet en question. (carotte r_lieu potager)*
	➤ Inverse :	*r_lieu-1*

* **r_instr** (action>instrument) ^16^:
	➤ Définition :	*L'instrument est l'objet avec lequel on fait l'action. Dans - Il mange sa salade avec une fourchette -, fourchette est l'instrument. Des instruments typiques de 'tuer' peuvent être 'arme', 'pistolet', 'poison', ... (couper r_instr couteau)*
	➤ Inverse :	*r_instr-1*

* **r_carac** (caractéristique) ^17^:
	➤ Définition :	*Pour un terme donné, souvent un objet, il est demandé d'en énumérer les CARACtéristiques (adjectifs) possibles/typiques. *
	➤ Example :	*'liquide', 'froide', 'chaude', pour 'eau'.*
	➤ Inverse :	*r_carac-1*

* **r_data** (r_data) ^18^:
	➤ Définition :	*Informations diverses (plutôt d'ordre lexicales)*

* **r_lemma** (r_lemma) ^19^:
	➤ Définition :	*Le lemme (par exemple 'mangent a pour lemme  'manger' ; 'avions' a pour lemme 'avion' ou 'avoir').*

* **r_has_magn** (magn) ^20^:
	➤ Définition :	*La magnification ou amplification, par exemple - forte fièvre - ou - fièvre de cheval - pour fièvre. Ou encore - amour fou - pour amour, - peur bleue - pour peur.*
	➤ Inverse :	*r_has_antimagn*

* **r_has_antimagn** (antimagn) ^21^:
	➤ Définition :	*L'inverse de la magnification, par exemple - bruine - pour pluie.*
	➤ Inverse :	*r_has_magn*

* **r_family** (famille) ^22^:
	➤ Définition :	*Des mots de la même famille lexicale sont demandés (dérivation morphologique, par exemple). *
	➤ Example :	*pour 'lait' on pourrait mettre 'laitier', 'laitage', 'laiterie', etc.*

* **r_carac-1** (caractéristique-1) ^23^:
	➤ Définition :	*Quels sont les objets (des noms) possédant typiquement/possiblement la caractérisque suivante ? *
	➤ Example :	*'soleil', 'feu', pour 'chaud'.*
	➤ Inverse :	*r_carac*

* **r_agent-1** (agent typique-1) ^24^:
	➤ Définition :	*Que peut faire ce SUJET ? (par exemple chat => miauler, griffer, etc.) (chat r_agent-1 manger)*
	➤ Inverse :	*r_agent*

* **r_instr-1** (instrument>action) ^25^:
	➤ Définition :	*L'instrument est l'objet avec lequel on fait l'action. Dans - Il mange sa salade avec une fourchette -, fourchette est l'instrument. On demande ici, ce qu'on peut faire avec un instrument donné... (scie r_instr-1 scier)*
	➤ Inverse :	*r_instr*

* **r_patient-1** (patient-1) ^26^:
	➤ Définition :	*(inverse de r_patient) Que peut-on faire à cet OBJET. Pour 'pomme', on pourrait avoir 'manger', 'croquer', couper', 'éplucher',  etc. (pomme r_patient-1 manger)*
	➤ Inverse :	*r_patient*

* **r_domain-1** (domaine-1) ^27^:
	➤ Définition :	*inverse de r_domain : à un domaine, on associe des termes*
	➤ Inverse :	*r_domain*

* **r_lieu-1** (lieu>chose) ^28^:
	➤ Définition :	*A partir d'un lieu, il est demandé d'énumérer ce qui peut typiquement s'y trouver. Par exemple : Paris r_lieu-1 tour Eiffel*
	➤ Inverse :	*r_lieu*

* **r_lieu_action** (lieu>action) ^30^:
	➤ Définition :	*A partir d'un lieu, énumérer les actions typiques possibles dans ce lieu.*
	➤ Inverse :	*r_action_lieu*

* **r_action_lieu** (action>lieu) ^31^:
	➤ Définition :	*A partir d'une action (un verbe), énumérer les lieux typiques possibles où peut être réalisée cette action.*
	➤ Inverse :	*r_lieu_action*

* **r_sentiment** (sentiment) ^32^:
	➤ Définition :	*Pour un terme donné, évoquer des mots liés à des SENTIMENTS ou des EMOTIONS que vous pourriez associer à ce terme. *
	➤ Example :	*la joie, le plaisir, le dégoût, la peur, la haine, l'amour, l'indifférence, l'envie, avoir peur, horrible, etc.*
	➤ Inverse :	*r_sentiment-1*

* **r_error** (erreur) ^33^:
	➤ Définition :	*lien d'erreur*

* **r_manner** (manière) ^34^:
	➤ Définition :	*De quelles MANIERES peut être effectuée l'action (le verbe) proposée. Il s'agira d'un adverbe ou d'un équivalent comme une locution adverbiale, par exemple : 'rapidement', 'sur le pouce', 'goulûment', 'salement' ... pour 'manger'.*
	➤ Inverse :	*r_manner-1*

* **r_meaning/glose** (glose/sens/signification) ^35^:
	➤ Définition :	*Quels SENS/SIGNIFICATIONS pouvez vous donner au terme proposé. Il s'agira de termes (des gloses) évoquant chacun des sens possibles, par exemple : 'forces de l'ordre', 'contrat d'assurance', 'police typographique', ... pour 'police'.*

* **r_infopot** (information potentielle) ^36^:
	➤ Définition :	*Information sémantique potentielle*

* **r_telic_role** (rôle télique) ^37^:
	➤ Définition :	*Le rôle télique indique la fonction du nom ou du verbe. *
	➤ Example :	*couper pour couteau, scier pour scie, etc. C'est le rôle qu'on lui destine communément pour un artéfact, ou bien un rôle qu'on peut attribuer à un objet naturel (réchauffer, éclairer pour soleil).*

* **r_agentif_role** (rôle agentif) ^38^:
	➤ Définition :	*De quelle(s)  manière(s)  peut être CRÉE/CONSTRUIT le terme suivant. On demande des verbes transitifs (le terme en est un complément d'objet) qui DONNENT NAISSANCE à l'entité désignée par le terme,  par exemple, 'construire' pour 'maison', 'rédiger'/'imprimer' pour 'livre' ou 'lettre'.*

* **r_verbe-action** (verbe>action) ^39^:
	➤ Définition :	*du verbe vers l'action. *
	➤ Example :	*construire -> construction , jardiner -> jardinage . C'est un terme directement dérivé (ayant la même racine). Applicable que pour un verbe et inverse de la relation 40 (action vers verbe).*
	➤ Inverse :	*r_action-verbe*

* **r_action-verbe** (action>verbe) ^40^:
	➤ Définition :	*de l'action vers le verbe. *
	➤ Example :	*construction -> construire, jardinage -> jardiner. C'est un terme directement dérivé (ayant la même racine). Applicable que pour un nom et inverse de la relation 39 (verbe vers action).*
	➤ Inverse :	*r_verbe-action*

* **r_has_conseq** (conséquence) ^41^:
	➤ Définition :	*B (que vous devez donner) est une CONSEQUENCE possible de A. A et B sont des verbes ou des noms.  Exemples : tomber -> se blesser ; faim -> voler ; allumer -> incendie ; négligence --> accident ; etc.*
	➤ Inverse :	*r_has_causatif*

* **r_has_causatif** (cause) ^42^:
	➤ Définition :	*B (que vous devez donner) est une CAUSE possible de A. A et B sont des verbes ou des noms.  Exemples : se blesser -> tomber ; vol -> pauvreté ; incendie -> négligence ; mort --> maladie ; etc.*
	➤ Inverse :	*r_has_conseq*

* **r_adj-verbe** (adj>verbe) ^43^:
	➤ Définition :	*Pour un adjectif de potentialité/possibilité, son verbe correspondant. Par exemple pour 'lavable' -> 'laver'*
	➤ Inverse :	*r_verbe-adj*

* **r_verbe-adj** (verbe>adj) ^44^:
	➤ Définition :	*Pour un verbe, son adjectif de potentialité/possibilité correspondant. Par exemple pour 'laver' -> 'lavable'*
	➤ Inverse :	*r_adj-verbe*

* **r_time** (action>temps) ^49^:
	➤ Définition :	*Donner une valeur temporelle -quel moment- peut-on associer au terme indiqué (par exemple 'dormir' -> nuit, 'bronzer' -> été, 'fatigue' -> 'soir')*

* **r_object>mater** (objet>matiere) ^50^:
	➤ Définition :	*Quel est la ou les MATIERE/SUBSTANCE pouvant composer l'objet qui suit. *
	➤ Example :	*'bois' pour 'poutre'.*
	➤ Inverse :	*r_mater>object*

* **r_mater>object** (matière>objet) ^51^:
	➤ Définition :	*Quel est la ou les CHOSES qui sont composés de la MATIERE/SUBSTANCE qui suit (exemple 'bois' -> poutre, table, ...).*
	➤ Inverse :	*r_object>mater*

* **r_successeur-time** (successeur temporel) ^52^:
	➤ Définition :	*Qu'est ce qui peut SUIVRE temporellement (par exemple Noêl -> jour de l'an, guerre -> paix, jour -> nuit,  pluie -> beau temps, repas -> sieste, etc) le terme suivant :*
	➤ Inverse :	*r_has_predecesseur-time*

* **r_make** (produit) ^53^:
	➤ Définition :	*Que peut PRODUIRE le terme ? (par exemple abeille -> miel, usine -> voiture, agriculteur -> blé,  moteur -> gaz carbonique ...)*
	➤ Inverse :	*r_product_of*

* **r_product_of** (est le produit de) ^54^:
	➤ Définition :	*Le terme est le RESULTAT/PRODUIT de qui/quoi ?*
	➤ Inverse :	*r_make*

* **r_against** (s'oppose à) ^55^:
	➤ Définition :	*A quoi le terme suivant S'OPPOSE/COMBAT/EMPECHE ? *
	➤ Example :	*un médicament s'oppose à la maladie.*
	➤ Inverse :	*r_against-1*

* **r_against-1** (a comme opposition) ^56^:
	➤ Définition :	*Inverse de r_against (s'oppose à) - a comme opposition active (S'OPPOSE/COMBAT/EMPECHE). *
	➤ Example :	*une bactérie à comme opposition antibiotique.*
	➤ Inverse :	*r_against*

* **r_implication** (implication) ^57^:
	➤ Définition :	*Qu'est-ce que le terme implique logiquement ? Par exemple : ronfler implique dormir, courir implique se déplacer, câlin implique contact physique. (attention ce n'est pas la cause ni le but...)*

* **r_quantificateur** (quantificateur) ^58^:
	➤ Définition :	*Quantificateur(s) typique(s) pour le terme,  indiquant une quantité. Par exemples, sucre -> grain, morceau - sel -> grain, pincée - herbe -> brin, touffe - ...*
	➤ Inverse :	*r_quantificateur-1*

* **r_masc** (équivalent masc) ^59^:
	➤ Définition :	*L'équivalent masculin du terme : lionne --> lion.*
	➤ Inverse :	*r_fem*

* **r_fem** (équivalent fem) ^60^:
	➤ Définition :	*L'équivalent féminin du terme : lion --> lionne.*
	➤ Inverse :	*r_masc*

* **r_equiv** (équivalent) ^61^:
	➤ Définition :	*Termes strictement équivalent/identique : acronymes et sigles (PS -> parti socialiste), apocopes (ciné -> cinéma), entités nommées (Louis XIV -> Le roi soleil), etc. (attention il ne s'agit pas de synonyme)*

* **r_manner-1** (maniere-1) ^62^:
	➤ Définition :	*Quelles ACTIONS (verbes) peut-on effectuer de cette manière ? *
	➤ Example :	*rapidement -> courir, manger, ...*
	➤ Inverse :	*r_manner*

* **r_agentive_implication** (implication agentive) ^63^:
	➤ Définition :	*Les verbes ou actions qui sont impliqués dans la création de l'objet. Par exemple pour 'construire' un livre, il faut, imprimer, relier, brocher, etc. Il s'agit des étapes nécessaires à la réalisation du rôle agentif.*

* **r_has_instance** (a pour instance) ^64^:
	➤ Définition :	*Une instance d'un 'type' est un individu particulier de ce type. Il s'agit d'une entité nommée (personne, lieu, organisation, etc) - par exemple, 'cheval' a pour instance possible 'Jolly Jumper', ou encore 'transatlantique' a pour instance possible 'Titanic'.*
	➤ Inverse :	*r_is_instance_of*

* **r_verb_real** (verbe>real) ^65^:
	➤ Définition :	*Pour un verbe, celui qui réalise l'action (par dérivation morphologique). *
	➤ Example :	*chasser -> chasseur, naviguer -> navigateur.*

* **r_chunk_head** (r_chunk_head) ^66^:
	➤ Définition :	**

* **r_similar** (similaire) ^67^:
	➤ Définition :	*Similaire/ressemble à ; par exemple le congre est similaire à une anguille, ...*

* **r_set>item** (ensemble>item) ^68^:
	➤ Définition :	*Quel est l'ELEMENT qui compose l'ENSEMBLE qui suit (par exemple, un essaim est composé d'abeilles)*
	➤ Inverse :	*r_item>set*

* **r_item>set** (item>ensemble) ^69^:
	➤ Définition :	*Quel est l'ENSEMBLE qui est composé de l'ELEMENT qui suit (par exemple, un essaim est composé d'abeilles)*
	➤ Inverse :	*r_set>item*

* **r_processus>agent** (processus>agent) ^70^:
	➤ Définition :	*Quel est l'acteur de ce processus/événement ? *
	➤ Example :	*'nettoyage' peut avoir comme acteur 'technicien de surface'.*
	➤ Inverse :	*r_processus>agent-1*

* **r_variante** (variante) ^71^:
	➤ Définition :	*Variantes du termes cible. *
	➤ Example :	*yaourt, yahourt, ou encore évènement, événement.*

* **r_syn_strict** (r_syn_strict) ^72^:
	➤ Définition :	*Termes strictement substituables, pour des termes hors du domaine général, et pour la plupart des noms (exemple : endométriose intra-utérine --> adénomyose)*

* **r_is_smaller_than** (est plus petit que) ^73^:
	➤ Définition :	*Qu'est-ce qui est physiquement plus gros que... (la comparaison doit être pertinente)*
	➤ Inverse :	*r_is_bigger_than*

* **r_is_bigger_than** (est plus gros que) ^74^:
	➤ Définition :	*Qu'est-ce qui est physiquement moins gros que... (la comparaison doit être pertinente)*
	➤ Inverse :	*r_is_smaller_than*

* **r_accomp** (accompagne) ^75^:
	➤ Définition :	*Est souvent accompagné de, se trouve avec... Par exemple : Astérix et Obelix, le pain et le fromage, les fraises et la chantilly.*

* **r_processus>patient** (processus>patient) ^76^:
	➤ Définition :	*Quel est le patient de ce processus/événement ? *
	➤ Example :	*'découpe' peut avoir comme patient 'viande'.*
	➤ Inverse :	*r_processus>patient-1*

* **r_verb_ppas** (r_verb_ppas) ^77^:
	➤ Définition :	*Le participe passé (au masculin singulier) du verbe infinitif. *
	➤ Example :	*pour manger => mangé*

* **r_cohypo** (co-hyponyme) ^78^:
	➤ Définition :	*Il est demandé d'énumérer les CO-HYPONYMES du terme. *
	➤ Example :	*'chat' et 'tigre' sont des co-hyponymes (de 'félin').*
	➤ Inverse :	*r_hypo*

* **r_verb_ppre** (r_verb_ppre) ^79^:
	➤ Définition :	*Le participe présent(au masculin singulier) du verbe infinitif. *
	➤ Example :	*pour manger => mangeant*

* **r_processus>instr** (processus>instrument) ^80^:
	➤ Définition :	*Quel est l'instrument/moyen de ce processus/événement ? *
	➤ Example :	*'découpe' peut avoir comme instrument 'couteau'.*
	➤ Inverse :	*r_processus>instr-1*

* **r_pref_form** (preferred_form) ^81^:
	➤ Définition :	*Indique une forme préférée*

* **r_interact_with** (interact_with) ^82^:
	➤ Définition :	*Indique avec quoi antécédent peut interagir.*

* **r_alias** (alias) ^83^:
	➤ Définition :	*Indique que les deux termes sont identiques, le 2e est un alias du premier. Utile pour synchroniser  des termes ou raffinement (éventuellement poly).*

* **r_has_euphemisme** (has_euphemisme) ^84^:
	➤ Définition :	*Moins intense, euphémisme. Exemple : être mort => être fatigué*

* **r_der_morpho** (dérivation morphologique) ^99^:
	➤ Définition :	*Des termes dériviés morphologiquement sont demandés). *
	➤ Example :	*pour 'lait' on pourrait mettre 'laitier', 'laitage', 'laiterie', etc. (mais pas 'lactose'). Pour 'jardin', on mettra 'jardinier', 'jardinage', 'jardiner', etc.*

* **r_has_auteur** (a comme auteur) ^100^:
	➤ Définition :	*Quel est l'auteur de l'oeuvre suivante ?*
	➤ Inverse :	*r_has_auteur-1*

* **r_has_personnage** (a comme personnages) ^101^:
	➤ Définition :	*Quels sont les personnages présents dans l'oeuvre qui suit ?*

* **r_can_eat** (se nourrit de) ^102^:
	➤ Définition :	*De quoi peut se nourir l'animal suivant ?*

* **r_has_actors** (a comme acteurs) ^103^:
	➤ Définition :	*A comme acteurs (pour un film ou similaire).*

* **r_deplac_mode** (mode de déplacement) ^104^:
	➤ Définition :	*Mode de déplacement. chat r_deplac_node marche*

* **r_has_interpret** (a comme interprètes) ^105^:
	➤ Définition :	*Interprète de personnages (cinéma ou théâtre)*

* **r_has_color** (couleur) ^106^:
	➤ Définition :	*A comme couleur(s)... chat r_color noir*

* **r_has_cible** (a comme cible) ^107^:
	➤ Définition :	*Cible de la maladie : myxomatose => lapin, rougeole => enfant, ...*

* **r_has_symptomes** (a comme symptomes) ^108^:
	➤ Définition :	*Symptomes de la maladie : myxomatose => yeux rouges, rougeole => boutons, ...*
	➤ Inverse :	*r_symptomes-1*

* **r_has_predecesseur-time** (prédécesseur temporel) ^109^:
	➤ Définition :	*Qu'est ce qui peut PRECEDER temporellement (par exemple -  inverse de successeur) le terme suivant :*
	➤ Inverse :	*r_successeur-time*

* **r_has_diagnostic** (diagnostic) ^110^:
	➤ Définition :	*Diagnostic pour la maladie : diabète => prise de sang, rougeole => examen clinique, ...*

* **r_has_predecesseur-space** (prédécesseur) ^111^:
	➤ Définition :	*Qu'est ce qui peut PRECEDER spatialement (par exemple -  inverse de successeur spatial) le terme suivant :*
	➤ Inverse :	*r_has_successeur-space*

* **r_has_successeur-space** (successeur) ^112^:
	➤ Définition :	*Qu'est ce qui peut SUIVRE spatialement (par exemple Locomotive à vapeur -> tender, wagon etc.) le terme suivant :*
	➤ Inverse :	*r_has_predecesseur-space*

* **r_has_social_tie_with** (relation sociale/famille) ^113^:
	➤ Définition :	*Relation sociale/familliale entre les individus... (annotation pour la nature exacte : frère, mari, etc.) Julie Depardieu r_social_tie>fille Gérard Deparidieu ; Gérard Deparidieu r_social_tie>père Julie Depardieu*

* **r_tributary** (r_tributary) ^114^:
	➤ Définition :	*Tributaire de (physique ou spatial).*

* **r_sentiment-1** (sentiment-1) ^115^:
	➤ Définition :	*Pour un SENTIMENT ou EMOTION donné, il est demandé d'énumérer les termes que vous pourriez associer. *
	➤ Example :	*pour 'joie', on aurait 'cadeau', 'naissance', 'bonne nouvelle', etc.*
	➤ Inverse :	*r_sentiment*

* **r_linked-with** (linked-with) ^116^:
	➤ Définition :	*A quoi est-ce relié (un wagon est relié à un autre wagon ou à une locomotive) ?*

* **r_foncteur** (r_foncteur) ^117^:
	➤ Définition :	*La fonction de ce terme par rapport à d'autres. Pour les prépositions notamment, 'chez' => relation r_location. (demande un type de relation comme valeur)*

* **r_but** (r_but) ^119^:
	➤ Définition :	*But de l'action (nom ou verbe)*
	➤ Inverse :	*r_but-1*

* **r_but-1** (r_but-1) ^120^:
	➤ Définition :	*Quel sont les actions ou verbes qui ont le terme cible comme but ?*
	➤ Inverse :	*r_but*

* **r_own** (pers>possession) ^121^:
	➤ Définition :	*Que POSSEDE le terme suivant ? (un soldat possède un fusil, une cavalière des bottes, ...  soldat r_own fusil, ...)*
	➤ Inverse :	*r_own-1*

* **r_own-1** (possession>pers) ^122^:
	➤ Définition :	*Par qui ou quoi EST POSSEDE le terme suivant ? (par exemple, fusil r_own-1 soldat)*
	➤ Inverse :	*r_own*

* **r_verb_aux** (r_verb_aux) ^123^:
	➤ Définition :	*Auxiliaire utilisé pour ce verbe*

* **r_predecesseur-logic** (prédécesseur logique) ^124^:
	➤ Définition :	*Qu'est ce qui peut PRECEDER logiquement (par exemple : A précède B -  inverse de successeur logique) le terme suivant :*

* **r_successeur-logic** (successeur logique) ^125^:
	➤ Définition :	*Qu'est ce qui peut SUIVRE logiquement (par exemple A -> B, C etc.) le terme suivant :*

* **r_isa-incompatible** (r_isa-incompatible) ^126^:
	➤ Définition :	*Relation d'incompatibilité pour les génériques. Si A r_isa-incompatible B alors X ne peut pas être à la fois A et B ou alors X est polysémique. *
	➤ Example :	*poisson r_isa-incompatible oiseau. Colin est à la fois un oiseau et un poisson, donc colin est polysémique.*

* **r_incompatible** (r_incompatible) ^127^:
	➤ Définition :	*Relation d'incompatibilité, ne doivent pas être présents ensemble. *
	➤ Example :	*alcool r_incompatible antibiotique.*

* **r_node2relnode-in** (r_node2relnode-in) ^128^:
	➤ Définition :	*Relation entre un noeud (quelconque) et un noeud de relation (type = 10)  - connecte le noeud d'entrée - permet de rendre le graphe connexe même avec les annotations de relations*

* **r_require** (nécessite / requiert) ^129^:
	➤ Définition :	*Il est demandé d'énumérer les termes nécessaires au mot mot cible... *
	➤ Example :	*'se reposer' => 'calme', ou 'pain' => 'farine'.*

* **r_is_instance_of** (est une instance de) ^130^:
	➤ Définition :	*Une instance est un individu particulier. Il s'agit d'une entité nommée (personne, lieu, organisation, etc) - par exemple, 'Jolly Jumper' est une instance de 'cheval', 'Titanic' en est une de 'transatlantique'.*
	➤ Inverse :	*r_has_instance*

* **r_is_concerned_by** (est concerné par) ^131^:
	➤ Définition :	*A peut être concerné par B. *
	➤ Example :	*une personne a un rendez-vous a une maladie, une idée, une opinion, etc...*
	➤ Inverse :	*r_concerning*

* **r_symptomes-1** (est un symptome de) ^132^:
	➤ Définition :	*Inverse de symptômes de la maladie : myxomatose => yeux rouges, rougeole => boutons, ...*
	➤ Inverse :	*r_has_symptomes*

* **r_units** (a pour unités) ^133^:
	➤ Définition :	*A comme unités pour une propriété, ou une mesure. Par exemple vitesse a pour unités m/s ou km/h, etc.*

* **r_promote** (favorise) ^134^:
	➤ Définition :	*Qu'est-ce que le terme suivant FAVORISE ? *
	➤ Example :	*un catalyseur favorise une réaction chimique.*
	➤ Inverse :	*r_promote-1*

* **r_circumstances** (circumstances) ^135^:
	➤ Définition :	*Les circonstances possibles pour un événements, ou un objet*

* **r_has_auteur-1** (est l'auteur de) ^136^:
	➤ Définition :	*Quel sont les oeuvres de l'auteur suivant ?*
	➤ Inverse :	*r_has_auteur*

* **r_processus>agent-1** (processus>agent-1) ^137^:
	➤ Définition :	**
	➤ Inverse :	*r_processus>agent*

* **r_processus>patient-1** (processus>patient-1) ^138^:
	➤ Définition :	**
	➤ Inverse :	*r_processus>patient*

* **r_processus>instr-1** (processus>instrument-1) ^139^:
	➤ Définition :	**
	➤ Inverse :	*r_processus>instr*

* **r_node2relnode-out** (r_node2relnode-out) ^140^:
	➤ Définition :	*Relation entre un noeud (quelconque) et un noeud de relation (type = 10) - connecte le noeud de sortie - permet de rendre le graphe connexe même avec les annotations de relations*

* **r_carac_nominale** (caractéristique nominale) ^141^:
	➤ Définition :	*Pour un terme donné, souvent un objet, il est demandé d'en énumérer les CARACtéristiques nominales (nom) possibles/typiques. *
	➤ Example :	*stylo => bille, feutre*

* **r_has_topic** (r_has_topic) ^142^:
	➤ Définition :	*Thème lié à l'objet de départ, exemples : restaurant r_has_topic sushis, magazine r_has_topic bande dessinée*

* **r_pourvoyeur** (action>pourvoyeur) ^148^:
	➤ Définition :	*Le pourvoyeur est l'entité qui fournit l'object de l'action (le pourvoyeur est un complément d'objet indirect introduit par 'à', ...). Par exemple dans - Le client demande une pizza à la serveuse - le pourvoyeur est ici la serveuse ...*

* **r_compl_agent** (complément d'agent) ^149^:
	➤ Définition :	*Le complément d'agent est celui qui effectue l'action dans les formes passives. *
	➤ Example :	*pour 'être mangé', la souris est l'agent et le chat le complément d'agent.*

* **r_has_beneficiaire** (action>bénéficiaire) ^150^:
	➤ Définition :	*Le bénéficiaire est l'entité qui tire bénéfice/préjudice de l'action (un complément d'objet indirect introduit par 'à', 'pour', ...). Par exemple dans - La sorcière donne une pomme à Blanche Neige -, la bénéficiaire est Blanche Neige ... enfin, bref, vous avez compris l'idée.*

* **r_descend_de** (descend de) ^151^:
	➤ Définition :	*Descend de (évolution)...*

* **r_domain_subst** (domain_subst) ^152^:
	➤ Définition :	*Quels sont le ou les domaines de substitution pour ce terme quand il est utilisé comme domaine (par exemple, 'muscle' => 'anatomie du système musculaire')*

* **r_has_prop** (propriété) ^153^:
	➤ Définition :	*Pour le terme donné, il faut indiquer les noms de propriétés pertinents (par exemple pour 'voiture', le 'prix', la 'puissance', la 'longueur', le 'poids', etc. On ne met que des noms et pas des adjectifs).*
	➤ Inverse :	*r_has_prop-1*

* **r_activ_voice** (voix active) ^154^:
	➤ Définition :	*Pour un verbe à la voix passive, sa voix active. *
	➤ Example :	*pour 'être mangé' on aura 'manger'.*

* **r_make_use_of** (r_make_use_of) ^155^:
	➤ Définition :	*Peut utiliser un objet ou produit (par exemple électricité pour frigo).*
	➤ Inverse :	*r_is_used_by*

* **r_is_used_by** (r_is_used_by) ^156^:
	➤ Définition :	*Est utilisé par (par exemple essence pour voiture).*
	➤ Inverse :	*r_make_use_of*

* **r_adj-nomprop** (adj>nomprop) ^157^:
	➤ Définition :	*Pour un adjectif, donner le nom de propriété correspondant. *
	➤ Example :	*pour 'friable' -> 'friabilité'*
	➤ Inverse :	*r_nomprop-adj*

* **r_nomprop-adj** (nomprop>adj) ^158^:
	➤ Définition :	*Pour un nom de propriété, donner l'adjectif correspondant. *
	➤ Example :	*pour 'friabilité' -> 'friable'*
	➤ Inverse :	*r_adj-nomprop*

* **r_adj-adv** (adj>adv) ^159^:
	➤ Définition :	*Pour un adjectif, donner l'adverbe correspondant. *
	➤ Example :	*pour 'rapide' -> 'rapidement'*
	➤ Inverse :	*r_adv-adj*

* **r_adv-adj** (adv>adj) ^160^:
	➤ Définition :	*Pour un adverbe, donner l'adjectif correspondant. *
	➤ Example :	*pour 'rapidement' -> 'rapide'*
	➤ Inverse :	*r_adj-adv*

* **r_homophone** (homophone) ^161^:
	➤ Définition :	*Il est demandé d'énumérer les homophones ou quasi-homophones de ce terme.*

* **r_potential_confusion_with** (confusion potentielle) ^162^:
	➤ Définition :	*Confusion potentielle avec un autre terme (par exemple, acre et âcre, détonner et détoner).*

* **r_concerning** (concernant) ^163^:
	➤ Définition :	*Qui concerne quelque chose ou quelqu'un. Par exemple: maladie r_concerning personne, ou disparition r_concerning emploi. (inverse de r_is_concerned_by)*
	➤ Inverse :	*r_is_concerned_by*

* **r_adj>nom** (r_adj>nom) ^164^:
	➤ Définition :	*Le nom associé à l'adjectif. *
	➤ Example :	*'urinaire' -> 'urine'*
	➤ Inverse :	*r_nom>adj*

* **r_nom>adj** (r_nom>adj) ^165^:
	➤ Définition :	*L'adjectif associé au nom. *
	➤ Example :	*'urine' -> 'urinaire'*
	➤ Inverse :	*r_adj>nom*

* **r_opinion_of** (r_opinion_of) ^166^:
	➤ Définition :	*L'opinion de tel groupe ou telle personne. Utilisé comme relation d'annotation.*

* **r_has_value** (r_has_value) ^167^:
	➤ Définition :	*Une valeur associée à une propriété ou un objet*

* **r_has_value>** (r_has_value>) ^168^:
	➤ Définition :	*Une valeur associée à une propriété ou un objet*

* **r_has_value<** (r_has_value<) ^169^:
	➤ Définition :	*Une valeur associée à une propriété ou un objet*

* **r_sing_form** (r_sing_from) ^170^:
	➤ Définition :	*La forme au singulier d'un terme. Exemple : chevaux r_sing_from cheval (pas de relation inverse)*

* **r_lieu>origine** (chose>lieu>origine) ^171^:
	➤ Définition :	*A pour origine B, saucisse de Toulouse r_lieu>origine Toulouse*

* **r_depict** (depiction) ^172^:
	➤ Définition :	*Que représente le mot ? (depiction) A représente B, par exemple une photo représente une personne, un visage, un paysage, etc.*

* **r_has_prop-1** (propriété-1) ^173^:
	➤ Définition :	*Pour propriété donnée, il faut indiquer les noms de choses pertinentes ayant cette propriété  (inverse de r_has_prop).*
	➤ Inverse :	*r_has_prop*

* **r_quantificateur-1** (quantificateur-1) ^174^:
	➤ Définition :	*inverse de r_quantificateur*
	➤ Inverse :	*r_quantificateur*

* **r_context** (r_context) ^200^:
	➤ Définition :	*Relation de contexte entre un terme et un noeud contexte.*

* **r_pos_seq** (POS_Seq) ^222^:
	➤ Définition :	*Séquence de parties du discours (Nom, Verbe, Adjectif, Adverbe, etc.). Exemple : belle maison => Adj: Nom:*

* **r_translation** (r_translation) ^333^:
	➤ Définition :	*Traduction vers une autre langue.*

* **r_link** (r_link) ^444^:
	➤ Définition :	*Lien vers une ressource externe (WordNet, RadLex, UMLS, Wikipedia, etc...)*

* **r_cooccurrence** (r_cooccurrence) ^555^:
	➤ Définition :	*co-occurences (non utilisée)*

* **r_aki** (r_aki) ^666^:
	➤ Définition :	*(TOTAKI) equivalent pour TOTAKI de l'association libre*

* **r_wiki** (r_wiki) ^777^:
	➤ Définition :	*Associations issues de wikipedia...*

* **r_annotation_exception** (r_annotation_exception) ^997^:
	➤ Définition :	*Relation pour indiquer qu'il s'agit d'une exception par rapport à la cible.  L'autruche ne vole pas, et c'est une exception par rapport à l'oiseau prototypique.*

* **r_annotation** (r_annotation) ^998^:
	➤ Définition :	*Relation pour annoter (de façon générale) des relations*

* **r_inhib** (r_inhib) ^999^:
	➤ Définition :	*relation d'inhibition, le terme inhibe les termes suivants... ce terme a tendance à exclure le terme associé.*

* **r_raff_sem-1** (r_raff_sem-1) ^2000^:
	➤ Définition :	*Inverse de r_raff_sem (automatique)*
	➤ Inverse :	*r_raff_sem*

* **r_promote-1** (est favorisé par) ^175^:
	➤ Définition :	*Par quoi le terme suivant est favorisé ? *
	➤ Example :	*une réaction chimique est favorisée par un catalyseur.*
	➤ Inverse :	*r_promote*

