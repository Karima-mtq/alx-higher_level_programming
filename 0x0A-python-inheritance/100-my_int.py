{"payload":{"allShortcutsEnabled":false,"fileTree":{"0x0A-python-inheritance":{"items":[{"name":"__pycache__","path":"0x0A-python-inheritance/__pycache__","contentType":"directory"},{"name":"tests","path":"0x0A-python-inheritance/tests","contentType":"directory"},{"name":"0-lookup.py","path":"0x0A-python-inheritance/0-lookup.py","contentType":"file"},{"name":"0-main.py","path":"0x0A-python-inheritance/0-main.py","contentType":"file"},{"name":"1-main.py","path":"0x0A-python-inheritance/1-main.py","contentType":"file"},{"name":"1-my_list.py","path":"0x0A-python-inheritance/1-my_list.py","contentType":"file"},{"name":"10-main.py","path":"0x0A-python-inheritance/10-main.py","contentType":"file"},{"name":"10-square.py","path":"0x0A-python-inheritance/10-square.py","contentType":"file"},{"name":"100-main.py","path":"0x0A-python-inheritance/100-main.py","contentType":"file"},{"name":"100-my_int.py","path":"0x0A-python-inheritance/100-my_int.py","contentType":"file"},{"name":"101-add_attribute.py","path":"0x0A-python-inheritance/101-add_attribute.py","contentType":"file"},{"name":"101-main.py","path":"0x0A-python-inheritance/101-main.py","contentType":"file"},{"name":"11-main.py","path":"0x0A-python-inheritance/11-main.py","contentType":"file"},{"name":"11-square.py","path":"0x0A-python-inheritance/11-square.py","contentType":"file"},{"name":"2-is_same_class.py","path":"0x0A-python-inheritance/2-is_same_class.py","contentType":"file"},{"name":"2-main.py","path":"0x0A-python-inheritance/2-main.py","contentType":"file"},{"name":"3-is_kind_of_class.py","path":"0x0A-python-inheritance/3-is_kind_of_class.py","contentType":"file"},{"name":"3-main.py","path":"0x0A-python-inheritance/3-main.py","contentType":"file"},{"name":"4-inherits_from.py","path":"0x0A-python-inheritance/4-inherits_from.py","contentType":"file"},{"name":"4-main.py","path":"0x0A-python-inheritance/4-main.py","contentType":"file"},{"name":"5-base_geometry.py","path":"0x0A-python-inheritance/5-base_geometry.py","contentType":"file"},{"name":"5-main.py","path":"0x0A-python-inheritance/5-main.py","contentType":"file"},{"name":"6-base_geometry.py","path":"0x0A-python-inheritance/6-base_geometry.py","contentType":"file"},{"name":"6-main.py","path":"0x0A-python-inheritance/6-main.py","contentType":"file"},{"name":"7-base_geometry.py","path":"0x0A-python-inheritance/7-base_geometry.py","contentType":"file"},{"name":"7-main.py","path":"0x0A-python-inheritance/7-main.py","contentType":"file"},{"name":"8-main.py","path":"0x0A-python-inheritance/8-main.py","contentType":"file"},{"name":"8-rectangle.py","path":"0x0A-python-inheritance/8-rectangle.py","contentType":"file"},{"name":"9-main.py","path":"0x0A-python-inheritance/9-main.py","contentType":"file"},{"name":"9-rectangle.py","path":"0x0A-python-inheritance/9-rectangle.py","contentType":"file"},{"name":"README.md","path":"0x0A-python-inheritance/README.md","contentType":"file"}],"totalCount":31},"":{"items":[{"name":"0x00-python-hello_world","path":"0x00-python-hello_world","contentType":"directory"},{"name":"0x01-python-if_else_loops_functions","path":"0x01-python-if_else_loops_functions","contentType":"directory"},{"name":"0x02-python-import_modules","path":"0x02-python-import_modules","contentType":"directory"},{"name":"0x03-python-data_structures","path":"0x03-python-data_structures","contentType":"directory"},{"name":"0x04-python-more_data_structures","path":"0x04-python-more_data_structures","contentType":"directory"},{"name":"0x05-python-exceptions","path":"0x05-python-exceptions","contentType":"directory"},{"name":"0x06-python-classes","path":"0x06-python-classes","contentType":"directory"},{"name":"0x07-python-test_driven_development","path":"0x07-python-test_driven_development","contentType":"directory"},{"name":"0x08-python-more_classes","path":"0x08-python-more_classes","contentType":"directory"},{"name":"0x09-python-everything_is_object","path":"0x09-python-everything_is_object","contentType":"directory"},{"name":"0x0A-python-inheritance","path":"0x0A-python-inheritance","contentType":"directory"},{"name":"0x0B-python-input_output","path":"0x0B-python-input_output","contentType":"directory"},{"name":"0x0C-python-almost_a_circle","path":"0x0C-python-almost_a_circle","contentType":"directory"},{"name":"0x0E-SQL_more_queries","path":"0x0E-SQL_more_queries","contentType":"directory"},{"name":"0x0F-python-object_relational_mapping","path":"0x0F-python-object_relational_mapping","contentType":"directory"},{"name":"0x10-python-network_0","path":"0x10-python-network_0","contentType":"directory"},{"name":"0x11-python-network_1","path":"0x11-python-network_1","contentType":"directory"},{"name":"0x12-javascript-warm_up","path":"0x12-javascript-warm_up","contentType":"directory"},{"name":"0x13-javascript_objects_scopes_closures","path":"0x13-javascript_objects_scopes_closures","contentType":"directory"},{"name":"README.md","path":"README.md","contentType":"file"}],"totalCount":20}},"fileTreeProcessingTime":4.02378,"foldersToFetch":[],"repo":{"id":571730234,"defaultBranch":"master","name":"alx-higher_level_programming","ownerLogin":"Jemal-Tilahun","currentUserCanPush":false,"isFork":false,"isEmpty":false,"createdAt":"2022-11-28T19:07:49.000Z","ownerAvatar":"https://avatars.githubusercontent.com/u/111070972?v=4","public":true,"private":false,"isOrgOwned":false},"symbolsExpanded":false,"treeExpanded":true,"refInfo":{"name":"master","listCacheKey":"v0:1669670545.178943","canEdit":false,"refType":"branch","currentOid":"3f8bd56a15e8a32e770ef83c3a33c36b6e763123"},"path":"0x0A-python-inheritance/100-my_int.py","currentUser":null,"blob":{"rawLines":["#!/usr/bin/python3","\"\"\"this module defines a class MyInt that inherits from int\"\"\"","","","class MyInt(int):","    \"\"\"Invert int operators == and !=\"\"\"","","    def __eq__(self, value):","        \"\"\"Override == opeartor with != behavior\"\"\"","        return self.real != value","","    def __ne__(self, value):","        \"\"\"Override != operator with == behavior\"\"\"","        return self.real == value"],"stylingDirectives":[[{"start":0,"end":18,"cssClass":"pl-c"}],[{"start":0,"end":62,"cssClass":"pl-s"}],[],[],[{"start":0,"end":5,"cssClass":"pl-k"},{"start":6,"end":11,"cssClass":"pl-v"},{"start":12,"end":15,"cssClass":"pl-s1"}],[{"start":4,"end":40,"cssClass":"pl-s"}],[],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":14,"cssClass":"pl-en"},{"start":15,"end":19,"cssClass":"pl-s1"},{"start":21,"end":26,"cssClass":"pl-s1"}],[{"start":8,"end":51,"cssClass":"pl-s"}],[{"start":8,"end":14,"cssClass":"pl-k"},{"start":15,"end":19,"cssClass":"pl-s1"},{"start":20,"end":24,"cssClass":"pl-s1"},{"start":25,"end":27,"cssClass":"pl-c1"},{"start":28,"end":33,"cssClass":"pl-s1"}],[],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":14,"cssClass":"pl-en"},{"start":15,"end":19,"cssClass":"pl-s1"},{"start":21,"end":26,"cssClass":"pl-s1"}],[{"start":8,"end":51,"cssClass":"pl-s"}],[{"start":8,"end":14,"cssClass":"pl-k"},{"start":15,"end":19,"cssClass":"pl-s1"},{"start":20,"end":24,"cssClass":"pl-s1"},{"start":25,"end":27,"cssClass":"pl-c1"},{"start":28,"end":33,"cssClass":"pl-s1"}]],"csv":null,"csvError":null,"dependabotInfo":{"showConfigurationBanner":false,"configFilePath":null,"networkDependabotPath":"/Jemal-Tilahun/alx-higher_level_programming/network/updates","dismissConfigurationNoticePath":"/settings/dismiss-notice/dependabot_configuration_notice","configurationNoticeDismissed":null,"repoAlertsPath":"/Jemal-Tilahun/alx-higher_level_programming/security/dependabot","repoSecurityAndAnalysisPath":"/Jemal-Tilahun/alx-higher_level_programming/settings/security_analysis","repoOwnerIsOrg":false,"currentUserCanAdminRepo":false},"displayName":"100-my_int.py","displayUrl":"https://github.com/Jemal-Tilahun/alx-higher_level_programming/blob/master/0x0A-python-inheritance/100-my_int.py?raw=true","headerInfo":{"blobSize":"375 Bytes","deleteInfo":{"deleteTooltip":"You must be signed in to make or propose changes"},"editInfo":{"editTooltip":"You must be signed in to make or propose changes"},"ghDesktopPath":"https://desktop.github.com","gitLfsPath":null,"onBranch":true,"shortPath":"1e31ce3","siteNavLoginPath":"/login?return_to=https%3A%2F%2Fgithub.com%2FJemal-Tilahun%2Falx-higher_level_programming%2Fblob%2Fmaster%2F0x0A-python-inheritance%2F100-my_int.py","isCSV":false,"isRichtext":false,"toc":null,"lineInfo":{"truncatedLoc":"14","truncatedSloc":"10"},"mode":"executable file"},"image":false,"isCodeownersFile":null,"isPlain":false,"isValidLegacyIssueTemplate":false,"issueTemplateHelpUrl":"https://docs.github.com/articles/about-issue-and-pull-request-templates","issueTemplate":null,"discussionTemplate":null,"language":"Python","languageID":303,"large":false,"loggedIn":false,"newDiscussionPath":"/Jemal-Tilahun/alx-higher_level_programming/discussions/new","newIssuePath":"/Jemal-Tilahun/alx-higher_level_programming/issues/new","planSupportInfo":{"repoIsFork":null,"repoOwnedByCurrentUser":null,"requestFullPath":"/Jemal-Tilahun/alx-higher_level_programming/blob/master/0x0A-python-inheritance/100-my_int.py","showFreeOrgGatedFeatureMessage":null,"showPlanSupportBanner":null,"upgradeDataAttributes":null,"upgradePath":null},"publishBannersInfo":{"dismissActionNoticePath":"/settings/dismiss-notice/publish_action_from_dockerfile","releasePath":"/Jemal-Tilahun/alx-higher_level_programming/releases/new?marketplace=true","showPublishActionBanner":false},"rawBlobUrl":"https://github.com/Jemal-Tilahun/alx-higher_level_programming/raw/master/0x0A-python-inheritance/100-my_int.py","renderImageOrRaw":false,"richText":null,"renderedFileInfo":null,"shortPath":null,"symbolsEnabled":true,"tabSize":8,"topBannersInfo":{"overridingGlobalFundingFile":false,"globalPreferredFundingPath":null,"repoOwner":"Jemal-Tilahun","repoName":"alx-higher_level_programming","showInvalidCitationWarning":false,"citationHelpUrl":"https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-repository-on-github/about-citation-files","showDependabotConfigurationBanner":false,"actionsOnboardingTip":null},"truncated":false,"viewable":true,"workflowRedirectUrl":null,"symbols":{"timed_out":false,"not_analyzed":false,"symbols":[{"name":"MyInt","kind":"class","ident_start":90,"ident_end":95,"extent_start":84,"extent_end":374,"fully_qualified_name":"MyInt","ident_utf16":{"start":{"line_number":4,"utf16_col":6},"end":{"line_number":4,"utf16_col":11}},"extent_utf16":{"start":{"line_number":4,"utf16_col":0},"end":{"line_number":13,"utf16_col":33}}},{"name":"__eq__","kind":"function","ident_start":152,"ident_end":158,"extent_start":148,"extent_end":258,"fully_qualified_name":"MyInt.__eq__","ident_utf16":{"start":{"line_number":7,"utf16_col":8},"end":{"line_number":7,"utf16_col":14}},"extent_utf16":{"start":{"line_number":7,"utf16_col":4},"end":{"line_number":9,"utf16_col":33}}},{"name":"__ne__","kind":"function","ident_start":268,"ident_end":274,"extent_start":264,"extent_end":374,"fully_qualified_name":"MyInt.__ne__","ident_utf16":{"start":{"line_number":11,"utf16_col":8},"end":{"line_number":11,"utf16_col":14}},"extent_utf16":{"start":{"line_number":11,"utf16_col":4},"end":{"line_number":13,"utf16_col":33}}}]}},"copilotInfo":null,"copilotAccessAllowed":false,"csrf_tokens":{"/Jemal-Tilahun/alx-higher_level_programming/branches":{"post":"_uc7s2Ww_kDMrC6SITF7qb41N9MZpa6r1jyYkUHZYxUshC7QxBYMX1Oy3CQqj5TxCnLE-Ckxama_2ILPBeavVg"},"/repos/preferences":{"post":"JlvnDUy346nsHurrtfGYrfZ2Y3i1KdLVzOPqTy3vhctEVFXFcrkI2XxbiBiLLheeeOjIhitRoQGZVed7-mHgHA"}}},"title":"alx-higher_level_programming/0x0A-python-inheritance/100-my_int.py at master · Jemal-Tilahun/alx-higher_level_programming"}