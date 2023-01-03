import { ComponentFixture, TestBed } from '@angular/core/testing';

import { BissexFooterComponent } from './bissex-footer.component';

describe('BissexFooterComponent', () => {
  let component: BissexFooterComponent;
  let fixture: ComponentFixture<BissexFooterComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ BissexFooterComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(BissexFooterComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
