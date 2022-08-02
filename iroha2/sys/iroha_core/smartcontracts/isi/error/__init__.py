from .....rust import Enum, Struct, Tuple, Dict
FindError = Enum[("Asset", "iroha_data_model.asset.Id"), ("AssetDefinition", "iroha_data_model.asset.DefinitionId"), ("Account", "iroha_data_model.account.Id"), ("Domain", "iroha_data_model.domain.Id"), ("MetadataKey", "iroha_data_model.name.Name"), ("Block", "iroha_crypto.hash.HashOf"), ("Transaction", "iroha_crypto.hash.HashOf"), ("Context", str), ("Peer", "iroha_data_model.peer.Id"), ("Trigger", "iroha_data_model.trigger.Id"), ("Role", "iroha_data_model.role.Id")] 
Mismatch = Struct[("expected", "iroha_core.smartcontracts.isi.permissions.ValidatorType"), ("actual", "iroha_core.smartcontracts.isi.permissions.ValidatorType")]

