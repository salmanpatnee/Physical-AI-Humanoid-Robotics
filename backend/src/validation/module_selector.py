from typing import List, Dict, Any
from .models import Module
from .qdrant_connector import QdrantConnector


class ModuleSelector:
    """Handle logic for selecting and working with multiple collections/modules."""
    
    def __init__(self, qdrant_connector: QdrantConnector):
        self.qdrant_connector = qdrant_connector
    
    def get_all_modules(self) -> List[Module]:
        """Get all available modules from Qdrant."""
        return self.qdrant_connector.get_available_collections()
    
    def select_module_by_name(self, module_name: str) -> Module:
        """Select a specific module by name."""
        all_modules = self.qdrant_connector.get_available_collections()
        
        for module in all_modules:
            if module.qdrant_collection_name == module_name or module.title == module_name:
                return module
        
        raise ValueError(f"Module '{module_name}' not found in available collections")
    
    def select_modules_by_tags(self, tags: List[str]) -> List[Module]:
        """Select modules that match any of the provided tags."""
        all_modules = self.qdrant_connector.get_available_collections()
        
        # For now, we'll just return all modules since we're not storing tags in Qdrant
        # In a real implementation, tags would be stored in the module metadata
        matching_modules = []
        
        for module in all_modules:
            # If the module has tags and any match the requested tags
            if module.tags and any(tag in module.tags for tag in tags):
                matching_modules.append(module)
        
        return matching_modules
    
    def select_modules_by_validation_accuracy(self, min_accuracy: float) -> List[Module]:
        """Select modules with validation accuracy above the specified threshold."""
        all_modules = self.qdrant_connector.get_available_collections()
        
        # For now, we'll return all modules since validation accuracy isn't stored in Qdrant
        # This would be updated after running validation
        matching_modules = []
        
        for module in all_modules:
            if module.validation_accuracy >= min_accuracy:
                matching_modules.append(module)
        
        return matching_modules
    
    def select_best_module_for_query(self, query: str, candidate_modules: List[Module] = None) -> Module:
        """Select the most appropriate module for a given query."""
        if not candidate_modules:
            candidate_modules = self.qdrant_connector.get_available_collections()
        
        if not candidate_modules:
            raise ValueError("No candidate modules available")
        
        # For now, just return the first module
        # In a more sophisticated implementation, we might:
        # - Analyze the query for keywords that match module names/descriptions
        # - Use the module with the highest validation accuracy
        # - Use metadata to determine the best match
        
        # Basic implementation: look for keywords in module names/descriptions
        query_lower = query.lower()
        best_module = candidate_modules[0]  # Default to first module
        best_score = 0
        
        for module in candidate_modules:
            score = 0
            
            # Score based on keywords in title and description
            if any(keyword in module.title.lower() for keyword in query_lower.split()):
                score += 2
            if any(keyword in module.description.lower() for keyword in query_lower.split()):
                score += 1
            if module.tags:
                if any(keyword in module.tags for keyword in query_lower.split()):
                    score += 3
            
            if score > best_score:
                best_score = score
                best_module = module
        
        # If no keyword matches were found, return the first module as default
        return best_module if best_score > 0 else candidate_modules[0]
    
    def get_module_statistics(self, module_name: str) -> Dict[str, Any]:
        """Get statistics about a specific module."""
        try:
            # Get the collection info from Qdrant
            collection_info = self.qdrant_connector.client.get_collection(module_name)
            
            stats = {
                'collection_name': module_name,
                'vector_count': collection_info.points_count,
                'indexed_vectors': collection_info.indexed_vectors_count,
                'full_vectors': collection_info.points_count - collection_info.indexed_vectors_count,
                'config': {
                    'on_disk_payload': collection_info.config.params.on_disk_payload,
                    'hnsw_config': collection_info.config.hnsw_config.__dict__ if collection_info.config.hnsw_config else None,
                    'quantization_config': collection_info.config.quantization_config.__dict__ if collection_info.config.quantization_config else None,
                }
            }
            
            return stats
        except Exception as e:
            raise ValueError(f"Could not get statistics for module '{module_name}': {str(e)}")
    
    def rank_modules_by_relevance(self, query: str, all_modules: List[Module] = None) -> List[Module]:
        """Rank modules by relevance to the given query."""
        if not all_modules:
            all_modules = self.qdrant_connector.get_available_collections()
        
        # Create a list of (module, score) tuples
        scored_modules = []
        
        for module in all_modules:
            score = 0
            
            # Calculate relevance score based on various factors
            if query.lower() in module.title.lower():
                score += 10
            elif any(keyword in module.title.lower() for keyword in query.lower().split()):
                score += 5
            
            if query.lower() in module.description.lower():
                score += 5
            elif any(keyword in module.description.lower() for keyword in query.lower().split()):
                score += 2
            
            if module.tags:
                tag_matches = sum(1 for tag in module.tags if query.lower() in tag.lower())
                score += tag_matches * 3
            
            # Consider validation accuracy if available
            if module.validation_accuracy > 0:
                # Boost score based on accuracy
                score *= (0.5 + module.validation_accuracy / 2)  # Range: 0.5 to 1.0
            
            scored_modules.append((module, score))
        
        # Sort by score (descending) and return modules
        scored_modules.sort(key=lambda x: x[1], reverse=True)
        return [module for module, score in scored_modules]