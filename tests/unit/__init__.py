import lazy_loader


__getattr__, __dir__, __all__ = lazy_loader.attach_stub(__name__, __file__)

__all__ = ['TestMain', 'test_main']
